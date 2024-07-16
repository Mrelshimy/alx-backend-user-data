#!/usr/bin/env python3
""" Auth model module """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ Return a hashed password """
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email, password):
        """ Register a new user """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError(f"User {email} already exists")
        user = self._db.add_user(email, _hash_password(password))
        return user
