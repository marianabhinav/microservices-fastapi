import logging
from fastapi import HTTPException, status
from src.app.service.models.document_model import Document
from .db_connection.write_db import DBConnection

"""
Gets a DB Connection and pass on the data to write.

Args:
    document(Documents): Object model of class Documents.
"""
def insert_document(document: Document):
    try:
        dbconnection = DBConnection.get_instance()
        logging.debug("Database Connection:: Success.")
        dbconnection.write_data(document)
    except (ValueError, ConnectionError) as exception:
        logging.debug("Database Connection:: Failure.")
        logging.error(exception)
        raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Database Service Unavailable.")
