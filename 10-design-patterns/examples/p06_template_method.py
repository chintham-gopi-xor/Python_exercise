"""Template Method worked example: a data import pipeline with a fixed skeleton."""

import csv
import io
import json
from abc import ABC, abstractmethod


class DataImporter(ABC):
    def run(self, raw_text):
        """The template: the order of steps is fixed, the steps are customisable."""
        records = self.parse(raw_text)
        records = [r for r in records if self.is_valid(r)]
        return self.summarise(records)

    @abstractmethod
    def parse(self, raw_text):
        """Turn raw text into a list of dictionaries."""

    def is_valid(self, record):
        # Optional hook with a sensible default
        return True

    def summarise(self, records):
        return f"{len(records)} records imported"


class CsvImporter(DataImporter):
    def parse(self, raw_text):
        return list(csv.DictReader(io.StringIO(raw_text)))


class JsonImporter(DataImporter):
    def parse(self, raw_text):
        return json.loads(raw_text)

    def is_valid(self, record):
        return "id" in record


if __name__ == "__main__":
    csv_text = "id,name\n1,Ana\n2,Ben\n"
    json_text = '[{"id": 1}, {"name": "no id"}, {"id": 3}]'
    print(CsvImporter().run(csv_text))
    print(JsonImporter().run(json_text))
