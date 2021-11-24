from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_health():
    response = client.head("/")
    assert response.status_code == 200

def test_add_document():
    body = {
        "title" : "va1",
        "skills" : ["va1", "val2"],
        "job_description" : "val1"
        }
    response = client.post("/addDocument",
                           json=body)
    
    assert response.status_code == 201
    assert response.json() == {
        "Reponse": "Success"
    }

def test_add_skills_empty_body():
    body = {}
    response = client.post("/addDocument",
                           json=body)
    assert response.status_code == 422

def test_add_skills_invalid_title_key_body():
    body = {
        "dummy" : "va1",
        "skills" : ["va1", "val2"],
        "job_description" : "val1"
        }
    response = client.post("/addDocument",
                           json=body)
    assert response.status_code == 422
    
def test_add_skills_invalid_skills_key_body():
    body = {
        "title" : "va1",
        "dummy" : ["va1", "val2"],
        "job_description" : "val1"
        }
    response = client.post("/addDocument",
                           json=body)
    assert response.status_code == 422
    
def test_add_skills_invalid_job_description_key_body():
    body = {
        "title" : "va1",
        "skills" : ["va1", "val2"],
        "dummy" : "val1"
        }
    response = client.post("/addDocument",
                           json=body)
    assert response.status_code == 422

def test_add_skills_invalid_title_value_body():
    body = {
        "title" : ["val1"],
        "skills" : ["va1", "val2"],
        "job_description" : "val1"
        }
    response = client.post("/addDocument",
                           json=body)
    assert response.status_code == 422
    
def test_add_skills_invalid_skills_value_body():
    body = {
        "title" : "va1",
        "skills" : 1,
        "job_description" : "val1"
        }
    response = client.post("/addDocument",
                           json=body)
    assert response.status_code == 422
    
def test_add_skills_invalid_job_description_key_body():
    body = {
        "title" : "va1",
        "skills" : ["va1", "val2"],
        "job_description" : ["val1"]
        }
    response = client.post("/addDocument",
                           json=body)
    assert response.status_code == 422