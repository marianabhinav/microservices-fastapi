from fastapi import APIRouter
from src.app.service.insert_document_service import insert_document_data
from src.app.service.insert_skills_service import insert_skills_data
from src.app.service.models.document_model import Document



#Helps to create tags in the documentation.
router = APIRouter(tags=["document"])

"""
Endpoint to add document data to the database.
"""
@router.post("/addDocument", status_code=201)
async def add_document(document: Document):
    insert_document_data(document)
    insert_skills_data(document.skills)
    return {"Reponse" : "Success"}