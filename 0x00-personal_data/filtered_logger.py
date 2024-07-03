#!/usr/bin/env python3
""" Filtered logger module """
import re


def filter_datum(fields: list, redaction: str,
                 message: str, separator: str) -> str:
    """ Function to return log message obfuscated """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
