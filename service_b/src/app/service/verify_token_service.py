import configparser
import jwt
import logging
from jwt.exceptions import InvalidAudienceError, InvalidSignatureError
import requests
from pathlib import Path
from os import path
from fastapi import HTTPException, status

config = configparser.ConfigParser()
basepath = Path(__file__).parents[3]
config_file_path = path.abspath(path.join(basepath, 'resources', 'ConfigFile.properties'))
public_secret_key_path = path.abspath(path.join(basepath, 'resources', 'jwt-key.pub'))
config.read(config_file_path)

SECURITY_ALGORITHM = config.get("COMMON", "SECURITY_ALGORITHM")
PUBLIC_SECRET_KEY = open(public_secret_key_path).read()
AUD = config.get("COMMON", "SERVICE_B")

"""
Check for the validity of the token.
Args:
    access_token(str): Bearer token which needs to be validated against the service public key.
    
Returns:
    bool: True if token is valid.
    Throws different exception if token is valid but not intended for this service.
"""
def verify_token(access_token):
    try:
        jwt.decode(access_token, PUBLIC_SECRET_KEY, algorithms=[SECURITY_ALGORITHM],
                             audience=AUD)
        logging.debug("Verify Token Service:: Success.")
        return True
    except (InvalidAudienceError):
        logging.debug("Verify Token Service:: Failure.")
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid Token.")
    except (InvalidSignatureError):
        logging.debug("Verify Token Service:: Failure.")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized Token.")