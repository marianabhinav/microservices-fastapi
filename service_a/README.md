# Service A
This Microservice based on [FAST API](https://fastapi.tiangolo.com/) saves the document data provided by the user. It also makes a POST call on service B with skills data provided by the user in the request as payload.
Contains a RSA private key which will be used to sign the jwt token for the request to other microservice.

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
`Default: host="0.0.0.0", port=8001`


## Documentation
[Swagger UI](https://github.com/swagger-api/swagger-ui) documentation is available with endpoint:  
`host:port/docs`

## Tests Execution
Install the pytest by:
```bash
pip install pytest
```
Then once insdie the main folder i.e. **service_a** run:
```bash
python -m pytest
```