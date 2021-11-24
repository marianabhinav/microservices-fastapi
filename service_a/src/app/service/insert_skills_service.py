import logging
from os import path
from pathlib import Path
import requests
import json
import configparser

from fastapi import status
from src.app.service.get_access_token_service import get_access_token
from src.app.service.models.document_model import Document


config = configparser.ConfigParser()
basepath = Path(__file__).parents[3]
config_file_path = path.abspath(path.join(basepath, 'resources', 'ConfigFile.properties'))
config.read(config_file_path)
SERVICE_B_URL = config.get("SERVICE_B_DETAILS", "SERVICE_B_URL")
ENDPOINT_ADD_SKILLS = config.get("SERVICE_B_DETAILS", "ENDPOINT_ADD_SKILLS")
AUD = config.get("COMMON", "SERVICE_B")

"""
Calls Service B POST /addSkills API to post the skills.
A Bearer token is issued and is provided in the Authorization header.

Args:
    skills(list[str]): List of skills provided by the user in the Document.
    
Returns:
    boolean : True in any case since we don't want to achieve loose coupling, 
    and don't want our result to depend upon the result by Service B.
"""
def insert_skills_data(skills: list[str]):
    access_token = get_access_token(AUD)
    json_dict = {"skills" : skills}
    try:
        response = requests.post(SERVICE_B_URL + ENDPOINT_ADD_SKILLS,
                    headers={"Authorization": "Bearer {}".format(access_token)},
                    data=json.dumps(json_dict))
    except BaseException:
        logging.error("Unable to connect to Service B.")
        logging.debug("Add Skills Service B:: Failure.")
        return
        
    if response.status_code == status.HTTP_201_CREATED:
        logging.debug("Add Skills Service B:: Success.")
    else:
        logging.debug("Add Skills Service B:: Failure.")
    return True