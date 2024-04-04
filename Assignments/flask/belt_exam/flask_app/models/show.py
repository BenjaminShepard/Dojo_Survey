from flask import flash
from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Show:
    DB = 'tv_shows_schema'
    def __init__(self, form_data):
        self.id = form_data['id']
        self.title = form_data['title']
        self.network = form_data['network']
        self.release_date = form_data['release_date']
        self.comments = form_data['comments']
        self.created_at = form_data['created_at']
        self.updated_at = form_data['updated_at']
        self.user = None


    @staticmethod
    def form_is_valid(form_data):

        is_valid = True

        if len(form_data["title"]) == 0:
            is_valid = False
            flash("Please enter Title.")
        elif len(form_data["title"]) < 2:   #I deviated from the exam template and did 2 characters long becuse there are some tv shows with 2 letter names
            is_valid = False
            flash("Your Title must be at least two characters")
            
        if len(form_data["network"]) == 0:
            is_valid = False
            flash("Please enter network.")
        elif len(form_data["network"]) < 2:  #I deviated again slightly here as well and did 2 characters long because there are some networks with 2 character names such as 'FX'
            is_valid = False
            flash("Your network must be at least two characters")

        if len(form_data["release_date"]) == 0:
            flash("Please enter a valid release date.")
            is_valid = False
        else:
            try:
                datetime.strptime(form_data["release_date"], "%Y-%m-%d")
            except:
                flash("Invalid release date.")
                is_valid = False

        if len(form_data["comments"]) == 0:
            is_valid = False
            flash("Please enter Comments.")
        elif len(form_data["comments"]) < 3:
            is_valid = False
            flash("Your comments must be at least three characters")

        return is_valid

    @classmethod
    def find_all(cls):
        query = """SELECT * FROM shows JOIN users ON shows.user_id = users.id"""
        list_of_dicts = connectToMySQL(Show.DB).query_db(query)

        shows = []
        for each_dict in list_of_dicts:
            show = Show(each_dict)
            shows.append(show)
        return shows

    @classmethod
    def find_all_with_users(cls):
        query = """SELECT * FROM shows JOIN users ON shows.user_id = users.id"""

        list_of_dicts = connectToMySQL(Show.DB).query_db(query)

        shows = []
        for each_dict in list_of_dicts:
            show = Show(each_dict)
            user_data = {
                "id": each_dict["users.id"],
                "first_name": each_dict["first_name"],
                "last_name": each_dict["last_name"],
                "email": each_dict["email"],
                "password": each_dict["password"],
                "created_at": each_dict["users.created_at"],
                "updated_at": each_dict["users.updated_at"],
            }
            user = User(user_data)
            show.user = user
            shows.append(show)
        return shows

    @classmethod
    def find_by_id(cls, show_id):
        query = """SELECT * FROM shows WHERE id = %(show_id)s"""
        data = {"show_id": show_id}
        list_of_dicts = connectToMySQL(Show.DB).query_db(query, data)

        if len(list_of_dicts) == 0:
            return None

        show = Show(list_of_dicts[0])
        return show

    @classmethod
    def find_by_id_with_user(cls, show_id):
        query = """SELECT * FROM shows JOIN users ON shows.user_id = users.id 
        WHERE shows.id = %(show_id)s"""

        data = {"show_id": show_id}
        list_of_dicts = connectToMySQL(Show.DB).query_db(query, data)

        if len(list_of_dicts) == 0:
            return None

        show = Show(list_of_dicts[0])
        user_data = {
            "id": list_of_dicts[0]["users.id"],
            "first_name": list_of_dicts[0]["first_name"],
            "last_name": list_of_dicts[0]["last_name"],
            "email": list_of_dicts[0]["email"],
            "password": list_of_dicts[0]["password"],
            "created_at": list_of_dicts[0]["users.created_at"],
            "updated_at": list_of_dicts[0]["users.updated_at"],
        }
        show.user = User(user_data)
        return show

    @classmethod
    def create(cls, form_data):
        query = """INSERT INTO shows
        (title, network, release_date, comments, user_id, created_at, updated_at)
        VALUES
        (%(title)s, %(network)s, %(release_date)s, %(comments)s, %(user_id)s, NOW(), NOW());"""
        show_id = connectToMySQL(Show.DB).query_db(query, form_data)
        return show_id

    @classmethod
    def update(cls, form_data):
        query = """UPDATE shows
        SET
        title=%(title)s,
        network=%(network)s,
        release_date=%(release_date)s,
        comments=%(comments)s,
        created_at= NOW(),
        updated_at = NOW()
        WHERE id = %(show_id)s;"""
        connectToMySQL(Show.DB).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, show_id):
        query = """DELETE FROM shows WHERE id = %(show_id)s;"""
        data = {"show_id": show_id}
        connectToMySQL(Show.DB).query_db(query, data)
        return



