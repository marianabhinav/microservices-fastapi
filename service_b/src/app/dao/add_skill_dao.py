import logging
from fastapi import HTTPException, status
from src.app.service.models.skill_model import Skills
from .db_connection.write_db import DBConnection

"""
Gets a DB Connection and pass on the data to write.

Args:
    skill(Skills): Object model of class Skills.
"""
def insert_skills(skills: Skills):
    try:
        dbconnection = DBConnection.get_instance()
        logging.debug("Database Connection:: Success.")
        dbconnection.write_data(skills.skills)
    except (ValueError, ConnectionError) as exception:
        logging.debug("Database Connection:: Failure.")
        logging.error(exception)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Database Service Unavailable.")
