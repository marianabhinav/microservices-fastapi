from pydantic import BaseModel

"""
Act as a model class for document data received from the user.
"""
class Document(BaseModel):
    title: str
    skills: list[str]
    job_description: str