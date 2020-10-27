import json


class CLI:

    """
    CLI rendering functions.
    """

    def table(widths, data):

        """
        Render and return a table.
        """

        tableString = ""

        format = "".join(["{:<" + str(w) + "}" for w in widths])
        for row in data:
            tableString += format.format(*row) + "\n"

        return tableString

    def json(data):

        """
        Prettify and return JSON.
        """

        jsonString = str(data)

        return json.dumps(
            json.loads(jsonString.replace("'", '"')),
            indent=4,
            sort_keys=True,
        )
