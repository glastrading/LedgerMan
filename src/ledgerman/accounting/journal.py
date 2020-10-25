import datetime, json


class Journal:

    """
    Journals store transactions (note, amount, type etc).
    """

    def __init__(self):

        """
        Create a journal.
        """

        self.entries = []

    def __repr__(self):
        return json.dumps(
            json.loads(str(self.entries).replace("'", '"')), indent=4, sort_keys=True
        )

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

        entry["type"] = {1: "debit", -1: "credit"}[type]
        entry["date"] = date.strftime("%Y-%m-%d %H:%M:%S")
        entry["amount"] = str(amount)
        entry["result"] = str(resultBalance)
        entry["debit"] = str(debitAccount)
        entry["credit"] = str(creditAccount)
        entry["note"] = note

        self.entries += [entry]
