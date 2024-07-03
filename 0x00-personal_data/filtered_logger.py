#!/usr/bin/env python3
""" Filtered logger module """
import re


def filter_datum(fields, redaction, message, separator):
    """ Function to return log message obfuscated """
    for field in fields:
        message = re.sub(field+'=.*?'+separator,
                         field+'='+redaction+separator, message)
    return message
