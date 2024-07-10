#!/usr/bin/env python3
""" Basic Auth module for the API """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic Auth class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extract Authorization header data """

        if authorization_header is None or\
            not isinstance(authorization_header, str) or\
                authorization_header[0:6] != "Basic ":
            return None

        return authorization_header[6:]
