#!/usr/bin/env python3
""" encrypt password module """
import bcrypt


def hhash_password(password: str) -> bytes:
    """ method to has data using bcrypt"""
    password = password.encode()
    return bcrypt.hashpw(password, bcrypt.gensalt())
