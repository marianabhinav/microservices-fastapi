import configparser
from os import path
from pathlib import Path
import jwt
import logging
from datetime import datetime, timedelta

config = configparser.ConfigParser()
basepath = Path(__file__).parents[3]
config_file_path = path.abspath(path.join(basepath, 'resources', 'ConfigFile.properties'))
private_secret_key_path = path.abspath(path.join(basepath, 'resources', 'jwt-key'))
config.read(config_file_path)

ISS = config.get("COMMON", "SERVICE_A")
SECURITY_ALGORITHM = config.get("COMMON", "SECURITY_ALGORITHM")
PRIVATE_SECRET_KEY = open(private_secret_key_path).read()

"""
Creates a Bearer token with the private key. Also, including details like:
    iat: Time issued at.
    iss: Issuer of the token.
    aud: Audience for which this token can be subjected to.
Args:
    access_token(str): Bearer token which needs to be validated against the service public key.
    
Returns:
    bool: True if token is valid.
    Throws different exception if token is valid but not intended for this service.
"""
def get_access_token(aud):
    iat = datetime.utcnow()
    to_encode = {
        "iat": iat, "iss": ISS, "aud": aud
    }
    encoded_jwt = jwt.encode(to_encode, PRIVATE_SECRET_KEY, algorithm=SECURITY_ALGORITHM).decode('utf-8')
    logging.debug("JWT Token Generation:: Success")
    return encoded_jwt