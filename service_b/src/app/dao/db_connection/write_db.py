import csv
from os import path
from pathlib import Path

"""
Implements Singleton Design Pattern to create a DB connection
which can be shared between different services.
"""
class DBConnection:
    __instance = None
    @staticmethod
    def get_instance():
        if DBConnection.__instance == None:
            DBConnection()
        return DBConnection.__instance
    
    def __init__(self):
        if DBConnection.__instance != None:
            raise ValueError("This is singleton class.")
        else:
            DBConnection.__instance = self

    """
    Create query to the database.
    
    Args:
        data(list): A list of string which forms a tuple in the DB.
    """
    def write_data(self, data):
        basepath = Path(__file__).parents[4]
        database_path = path.abspath(path.join(basepath, 'database', 'skills.csv'))
        try:
            with open(database_path, "a+", newline="") as db:
                writer = csv.writer(db)
                writer.writerow(data)
        except EnvironmentError:
            raise ConnectionError("Unable to Write.")