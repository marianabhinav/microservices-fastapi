from pydantic import BaseModel

"""
Act as a model class for list of Skills data received from the user.
"""
class Skills(BaseModel):
    skills: list[str]