from src.app.dao.add_document_dao import insert_document
from src.app.service.models.document_model import Document

"""
A place holder for service module which takes the call from controller
and pass on to the dao layer.
Note: It was not actuall required in this particular case but implemented
        anyways to stick to the design pattern.

Args:
    document(Documents): Object model of class Documents.
"""
def insert_document_data(document: Document):
    insert_document(document)