from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer
from src.app.service.insert_skills_service import insert_skills_data

from src.app.service.models.skill_model import Skills
from src.app.service.verify_token_service import verify_token

#Helps to create tags in the documentation.
router = APIRouter(tags=["skills"])

token_auth_scheme = HTTPBearer(scheme_name='Authorization')

"""
Endpoint to add a list of skills to the database.
This call is encrypted via Bearer token.
"""
@router.post("/addSkills", status_code=201)
async def add_skills(skill: Skills,
                     authorization: str = Depends(token_auth_scheme)):
    verify_token(authorization.credentials)
    insert_skills_data(skill)
    return {"Reponse" : "Success"}