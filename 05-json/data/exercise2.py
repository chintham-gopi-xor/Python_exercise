import json
from pathlib import Path

config_path = Path("config.json")
with config_path.open(encoding="utf-8") as f:
    config = json.load(f)


def get_nested(data, path, default=None):
    current = data
    for key in path.split("."):
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current

queries = [
    ("app.name", None),
    ("server.port", None),
    ("server.timeouts.read", None),
    ("database.pool.max", None),
    ("features.beta_dashboard", None),
    ("cache.ttl", 60),
    ("server.host.name", "n/a"),
]


for path, default in queries:
    value = get_nested(config, path, default)
    print(f"{path} = {value!r}")

admins = get_nested(config, "admins", [])
print(f"admins: {', '.join(admins)} ({len(admins)})")