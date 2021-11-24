# Service B
This Microservice based on [FAST API](https://fastapi.tiangolo.com/) saves the data for the skills of a user.
Contains a RSA public key of available services which will be used to verify the jwt token for a valid request.

## Instructions to run
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the dependencies and run this service.

```bash
pip install -r requirements.txt
```

Run the main.py file to start the server

```bash
python main.py
```

FAST API server will start at the address mentioned in the **main.py**.  
`Default: host="0.0.0.0", port=8002`


## Documentation
[Swagger UI](https://github.com/swagger-api/swagger-ui) documentation is available with endpoint:  
`host:port/docs`

## Tests Execution
Install the pytest by:
```bash
pip install pytest
```
Then once insdie the main folder i.e. **service_b** run:
```bash
python -m pytest
```