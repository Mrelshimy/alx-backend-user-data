#!/usr/bin/env python3
""" Basic Auth module for the API """
from flask import request
from typing import List, TypeVar
from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Decode Base64 data from Auth header """

        if base64_authorization_header is None or\
                not isinstance(base64_authorization_header, str):
            return None

        try:
            result = base64.b64decode(base64_authorization_header,
                                      altchars=None)
            return result.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ Extract user credentials """

        if decoded_base64_authorization_header is None or\
            not isinstance(decoded_base64_authorization_header, str) or\
                ':' not in decoded_base64_authorization_header:
            return (None, None)
        (username, password) = decoded_base64_authorization_header.split(':')
        return (username, password)
