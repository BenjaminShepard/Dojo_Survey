from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint

class Dojo:
    _DB = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def find_all(cls):
        
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(Dojo._DB).query_db(query)
        pprint(results)

        dojos = []
        for each_dojo in results:
            dojo = Dojo(each_dojo)
            dojos.append(dojo)
        return dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = """
            INSERT INTO dojos
            (name, created_at, updated_at)
            VALUES (%(name)s, NOW(), NOW());
            """
        result = connectToMySQL(cls._DB).query_db(query, data)
        return result





