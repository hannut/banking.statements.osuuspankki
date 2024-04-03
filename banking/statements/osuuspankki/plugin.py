# -*- encoding: utf-8 -*-

from ofxstatement.plugin import Plugin

from .parser import SIGNATURES, OPCsvStatementParser


class OPPlugin(Plugin):  # pylint: disable=too-few-public-methods
    "Suomen Osuuspankki / Finnish Osuuspankki"

    def get_parser(self, filename):
        with open(filename, "r", encoding="utf-8") as file:
            signature = file.readline().strip()
            file.seek(0)
            if signature in SIGNATURES:
                parser = OPCsvStatementParser(file)
                parser.statement.account_id = self.settings["account"]
                parser.statement.currency = self.settings["currency"]
                parser.statement.bank_id = self.settings.get("bank", "Osuuspankki")
                return parser

        # If no plugin with matching signature was found
        raise ValueError(
            "No suitable Osuuspankki parser found for this statement file."
        )
