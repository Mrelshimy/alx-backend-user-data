#!/usr/bin/env python3
""" Auth model module """
import bcrypt


def _hash_password(password: str) -> str:
    """ Return a hashed password """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
