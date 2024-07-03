#!/usr/bin/env python3
""" Filtered logger module """
import logging
import re
from typing import List


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formatter method to format incoming logs """
        record = super(RedactingFormatter, self).format(record)
        record = filter_datum(self.fields, self.REDACTION,
                              record, self.SEPARATOR)
        return record


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """ Function to return log message obfuscated """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
