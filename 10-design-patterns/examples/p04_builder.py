"""Builder worked example: build an email message step by step."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class EmailMessage:
    to: tuple
    subject: str
    body: str
    cc: tuple = ()
    attachments: tuple = field(default_factory=tuple)


class EmailBuilder:
    def __init__(self):
        self._to = []
        self._cc = []
        self._subject = ""
        self._body = ""
        self._attachments = []

    # Each step returns self so calls can be chained (a "fluent" interface)
    def to(self, address):
        self._to.append(address)
        return self

    def cc(self, address):
        self._cc.append(address)
        return self

    def subject(self, text):
        self._subject = text
        return self

    def body(self, text):
        self._body = text
        return self

    def attach(self, filename):
        self._attachments.append(filename)
        return self

    def build(self):
        if not self._to:
            raise ValueError("an email needs at least one recipient")
        if not self._subject:
            raise ValueError("an email needs a subject")
        return EmailMessage(
            tuple(self._to), self._subject, self._body,
            tuple(self._cc), tuple(self._attachments),
        )


if __name__ == "__main__":
    mail = (
        EmailBuilder()
        .to("ana@example.com")
        .to("ben@example.com")
        .cc("boss@example.com")
        .subject("Quarterly report")
        .body("Please find the report attached.")
        .attach("q3.pdf")
        .build()
    )
    print(mail)
    try:
        EmailBuilder().subject("No recipient").build()
    except ValueError as err:
        print("Error:", err)
