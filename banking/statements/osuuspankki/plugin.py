# -*- encoding: utf-8 -*-
import csv
import decimal
import sys
from importlib import import_module
from io import StringIO

from ofxstatement.plugin import Plugin, PluginNotRegistered

from .parser import SIGNATURES, OPCsvStatementParser


class OPPlugin(Plugin):
    "Suomen Osuuspankki / Finnish Osuuspankki"

    def get_parser(self, fin):
        f = open(fin, "r", encoding="utf-8")
        signature = f.readline().strip()
        f.seek(0)
        if signature in SIGNATURES:
            parser = OPCsvStatementParser(f)
            parser.statement.account_id = self.settings["account"]
            parser.statement.currency = self.settings["currency"]
            parser.statement.bank_id = self.settings.get("bank", "Osuuspankki")
            return parser

        # no plugin with matching signature was found
        raise Exception("No suitable Osuuspankki parser found for this statement file.")
