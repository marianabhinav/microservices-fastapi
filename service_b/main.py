from os import path
from pathlib import Path
import uvicorn
import logging
from fastapi import FastAPI
from src.app.contorller import add_skill_controller

basepath = Path(__file__).parent
log_file_path = path.abspath(path.join(basepath, 'logs', 'logfile.log'))
logging.basicConfig(filename=log_file_path,
                    format="%(asctime)s %(message)s",
                    level=logging.DEBUG)

app = FastAPI()

#Includes routes from other mentioned controller files.
app.include_router(
    add_skill_controller.router)

"""
Health call to check the status of the application.
"""
@app.head("/")
async def health_check():
    logging.debug("Health Check:: Success.")
    return {"Success."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)