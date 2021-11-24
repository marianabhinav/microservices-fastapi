from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health():
    response = client.head("/")
    assert response.status_code == 200

def test_add_skills():
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Mzc3MTUzMDAsImlzcyI6IlNFUlZJQ0VBIiwiYXVkIjoiU0VSVklDRUIifQ.j60KP4jRneUXIU7vQlJayUsbOJKQBFpKClsWGhX2qgzYWeK4AirdFHMExJ4g_41oijEg0PXKhm6wYiFuUFbkAw9UAJaqeAHvfzaZydEzq_wfH5kxTMpdCjyI3BEP-I6AsCA2a9L8lWnJLUJo1xfYFeht9PU1ypc1GWUbCPTeeL7o_uSKdRlbwRHTWbusP5IjZ74QMjoKSJjBDYCaksJTJMxqwG1G7PDGsU0LpFxrft80Z03Nrp0wVIWgjOfMLEvC7gIQmbCuA5ZdeVCWqn6rRa-wIe_u2IzVe4QCAVddVyVJylzJd4XijGVwzpM6sXhZBLNkoDjq7cNMkJ7ZKsdXg7kFc-tRA9hbeo0ecWHvQf8ZKKEOhY49wZlWUHWceYNTc49k_4VAZwh3wKChhXPHQDU9bOgkwdGakTVC_rAYH9TAgEYL7hWFSo1D341yidcZPb8MdU85fthjDcIKkI8slTST-7gsVMeNtjV9_zyCtNur8m8--bFgD4981HOIoj0dG6wsAuJeGtXNLt3GUHo5aNYV_gZeALwAXvh2FYOlhyyWOOEm4xr3R5fwezquNqw2BGT9SIz1zmwQwq1nR_K12aaqMlnlefKNqQVNm0YY5z0IM9UWOLxIgBPmDjwMtKZMxPeyl8aLuMX9vj-QY_42B8pX5klOe_xZqf7QacrryBc'
    body = {"skills" : ["va1", "val2"]}
    response = client.post("/addSkills", headers={"Authorization": "Bearer %s" % token},
                           json=body)
    assert response.status_code == 201
    assert response.json() == {
        "Reponse": "Success"
    }

def test_add_skills_unauth_token():
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Mzc3MTQ2NDIsImlzcyI6IlNFUlZJQ0VBIiwiYXVkIjoiU0VSVklDRUIifQ.ftGyc0D52wVHviKWgerYYDJHKSPTK3WjDrjBbFIHR2sUFetBxhH_1X0GBG6C5M5PYPaNegOg6O9EYck6KyiWcarOY8hWjBB1jPXuRLlNCZwDgk0-JT3kw6PpSjrmMqWd0yzVeLlMZ5wGXZeqjON13yza6KiX0hpux9BeRquCGWk'
    body = {"skills" : ["va1", "val2"]}
    response = client.post("/addSkills", headers={"Authorization": "Bearer %s" % token},
                           json=body)
    assert response.status_code == 401
    assert response.json() == {"detail": "Unauthorized Token."}


def test_add_skills_invalid_token():
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Mzc3MTE3ODksImlzcyI6IlNFUlZJQ0VBIiwiYXVkIjoiU0VSVklDRUMifQ.HCKwc0vcgoyHNHV9CmoFK-4sPwlm9ptF7SWdFkzCG13K499Oktl0m7r8jI6fEQE9HE4J247i2XMUYuF0dS0aLrU0Kt1Lavl9MlewPbgyhvu7KAcVZinccSMOpp3TKfYgYWbArpcPiu2dCinKOVfa521FgIFj-gtKbqOLJ0B1Xey7y6lmtMwvCs9o2LXP90jHb0QA4VUn7K4yUEuv0SY7iL1AStGphPkwP01LOfB5E1CUK-AM1Mo9YqAl5Am6WHQL0KqCyIhxpeKM9fVhp_4CTpB1GunLCdPO1i77OHBEEFfJ7-O4hiLMpyOLbKIh8fRO9IES6P9kY5BZdMX0gs21budKVy9BPihsFhUsoov572cd7dJcQ1nl2qeVEEFVwBjkZjxIvO6PhzCCTbmQW8DPHeokpk4vnP8L2LwQ0SW_MOVRtAhw2FjZ0YvcW89UXpRjbSK-1nROa484LxiIX2Eho4FfWcXbVuyhff9z5JsLz5MtiqJ1SdyMDkG0M3whnIcyYsY4fq0h8fZY14EKoXGNJUrJQrLc065x_sDIeOH57YJl-7sA34EaJ1RLxI84h509_6fMGTJRX9eP_IfUVOuEvRIolq7Y0VglpVb0NHV-k-CKi9WF_SSk4nfdzaFab0sL6Vvg4SVmFHZ-t2_1fg-T2MCxTNWhV58gC9qEFpGRNos'
    body = {"skills" : ["va1", "val2"]}
    response = client.post("/addSkills", headers={"Authorization": "Bearer %s" % token},
                           json=body)
    assert response.status_code == 403
    assert response.json() == {"detail": "Invalid Token."}

def test_add_skills_invalid_key_body():
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Mzc3MTUzMDAsImlzcyI6IlNFUlZJQ0VBIiwiYXVkIjoiU0VSVklDRUIifQ.j60KP4jRneUXIU7vQlJayUsbOJKQBFpKClsWGhX2qgzYWeK4AirdFHMExJ4g_41oijEg0PXKhm6wYiFuUFbkAw9UAJaqeAHvfzaZydEzq_wfH5kxTMpdCjyI3BEP-I6AsCA2a9L8lWnJLUJo1xfYFeht9PU1ypc1GWUbCPTeeL7o_uSKdRlbwRHTWbusP5IjZ74QMjoKSJjBDYCaksJTJMxqwG1G7PDGsU0LpFxrft80Z03Nrp0wVIWgjOfMLEvC7gIQmbCuA5ZdeVCWqn6rRa-wIe_u2IzVe4QCAVddVyVJylzJd4XijGVwzpM6sXhZBLNkoDjq7cNMkJ7ZKsdXg7kFc-tRA9hbeo0ecWHvQf8ZKKEOhY49wZlWUHWceYNTc49k_4VAZwh3wKChhXPHQDU9bOgkwdGakTVC_rAYH9TAgEYL7hWFSo1D341yidcZPb8MdU85fthjDcIKkI8slTST-7gsVMeNtjV9_zyCtNur8m8--bFgD4981HOIoj0dG6wsAuJeGtXNLt3GUHo5aNYV_gZeALwAXvh2FYOlhyyWOOEm4xr3R5fwezquNqw2BGT9SIz1zmwQwq1nR_K12aaqMlnlefKNqQVNm0YY5z0IM9UWOLxIgBPmDjwMtKZMxPeyl8aLuMX9vj-QY_42B8pX5klOe_xZqf7QacrryBc'
    body = {"dummyVal" : ["va1", "val2"]}
    response = client.post("/addSkills", headers={"Authorization": "Bearer %s" % token},
                           json=body)
    assert response.status_code == 422
    
def test_add_skills_invalid_list_body():
    token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Mzc3MTUzMDAsImlzcyI6IlNFUlZJQ0VBIiwiYXVkIjoiU0VSVklDRUIifQ.j60KP4jRneUXIU7vQlJayUsbOJKQBFpKClsWGhX2qgzYWeK4AirdFHMExJ4g_41oijEg0PXKhm6wYiFuUFbkAw9UAJaqeAHvfzaZydEzq_wfH5kxTMpdCjyI3BEP-I6AsCA2a9L8lWnJLUJo1xfYFeht9PU1ypc1GWUbCPTeeL7o_uSKdRlbwRHTWbusP5IjZ74QMjoKSJjBDYCaksJTJMxqwG1G7PDGsU0LpFxrft80Z03Nrp0wVIWgjOfMLEvC7gIQmbCuA5ZdeVCWqn6rRa-wIe_u2IzVe4QCAVddVyVJylzJd4XijGVwzpM6sXhZBLNkoDjq7cNMkJ7ZKsdXg7kFc-tRA9hbeo0ecWHvQf8ZKKEOhY49wZlWUHWceYNTc49k_4VAZwh3wKChhXPHQDU9bOgkwdGakTVC_rAYH9TAgEYL7hWFSo1D341yidcZPb8MdU85fthjDcIKkI8slTST-7gsVMeNtjV9_zyCtNur8m8--bFgD4981HOIoj0dG6wsAuJeGtXNLt3GUHo5aNYV_gZeALwAXvh2FYOlhyyWOOEm4xr3R5fwezquNqw2BGT9SIz1zmwQwq1nR_K12aaqMlnlefKNqQVNm0YY5z0IM9UWOLxIgBPmDjwMtKZMxPeyl8aLuMX9vj-QY_42B8pX5klOe_xZqf7QacrryBc'
    body = {"skills" : "val"}
    response = client.post("/addSkills", headers={"Authorization": "Bearer %s" % token},
                           json=body)
    assert response.status_code == 422