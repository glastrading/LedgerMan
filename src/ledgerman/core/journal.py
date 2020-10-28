import datetime
import json


class Journal:

    """
    Journals store transactions (note, amount, type etc).
    """

    # --- DATA MODEL METHODS --- #

    def __init__(self, *entries):

        """
        Create a journal.
        """

        self.entries = []

        for e in entries:
            self.entries += [e]

    def __repr__(self):
        return self.serialize()

    # --- SERIALIZATION METHODS --- #

    def serialize(self, indent=4, sort_keys=True):
        d = {
            "_type": "Journal",
            "entries": self.entries,
        }

        return json.dumps(d, indent=indent, sort_keys=sort_keys)

    @staticmethod
    def deserialize(d):
        if isinstance(d, str):
            d = json.loads(d)

        if d["_type"] != "Journal":
            raise ValueError("Cannot deserialize objects other than Journal.")

        return Journal(*d["entries"])

    # --- CLASS SPECIFIC METHODS --- #

    def log(
        self,
        type,
        resultBalance,
        amount,
        debitAccount,
        creditAccount,
        note="",
        date=None,
    ):

        """
        Log a transaction in a journal entry.
        """

        if date == None:
            date = datetime.datetime.now()
        elif isinstance(date, str):  # format: 2020-10-25 07:59:23
            date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        elif not isinstance(date, datetime.datetime):
            raise ValueError(
                "Expected a datetime object or string like '2020-10-25 07:59:23' as input date for Journal.log"
            )

        entry = {}

        from .account import Account

        entry["type"] = {Account.DEBIT: "debit", Account.CREDIT: "credit"}[
            Account.typeToInt(type)
        ]
        entry["date"] = date.strftime("%Y-%m-%d %H:%M:%S")
        entry["amount"] = str(amount)
        entry["result"] = str(resultBalance)
        entry["debit"] = debitAccount.name
        entry["credit"] = creditAccount.name
        entry["note"] = note

        self.entries += [entry]

    # --- DATA MODEL OPERATIONS --- #

    def __eq__(self, other):
        if type(other) != Journal:
            return False
        return self.entries == other.entries
