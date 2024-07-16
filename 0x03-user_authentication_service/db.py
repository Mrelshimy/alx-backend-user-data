#!/usr/bin/env python3
""" DB model module """
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError


class DB:
    """ DB class """

    def __init__(self) -> None:
        """ Initialize a new DB instance """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """ Memoized session object """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Add user to the db method """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """ Find user based on attribute method """
        users = self._session.query(User)
        for key, value in kwargs.items():
            if key not in User.__dict__:
                raise InvalidRequestError
            for user in users:
                if getattr(user, key) == value:
                    return user
        raise NoResultFound

    def update_user(self, user_id, **kwargs):
        """ Update user method """
        user = self.find_user_by(id=user_id)
        for key, value in kwargs.items():
            if key not in user.__dict__:
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
        return None
