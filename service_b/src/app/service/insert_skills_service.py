from src.app.dao.add_skill_dao import insert_skills
from src.app.service.models.skill_model import Skills

"""
A place holder for service module which takes the call from controller
and pass on to the dao layer.
Note: It was not actuall required in this particular case but implemented
        anyways to stick to the design pattern.

Args:
    skill(Skills): Object model of class Skills.
"""
def insert_skills_data(skills: Skills):
    insert_skills(skills)