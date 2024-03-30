from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint

class Ninja:
    _DB = "dojos_and_ninjas"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


@classmethod
def find_all(cls):

    query = "SELECT * FROM ninjas;"
    results = connectToMySQL(Ninja._DB).query_db(query)

    ninjas = []
    for each_ninja in results:
        ninja = Ninja(each_ninja)
        ninjas.append(ninja)
    return ninjas