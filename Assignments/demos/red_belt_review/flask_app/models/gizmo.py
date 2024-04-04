from flask import flash
from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User


class Gizmo:
    DB = ""

    def __init__(self, data):
        self.id = data["id"]
        self.column1 = data["column1"]
        self.column2 = data["column2"]
        self.column3 = data["column3"]
        self.column4 = data["column4"]
        self.column5 = data["column5"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None


@staticmethod
def form_is_valid(form_data):
    is_valid = True

    # text validator
    if len(form_data["column"]) == 0:
        flash("Please enter column")
        is_valid = False
    elif len(form_data["column"]) < 3:
        flash("Column must be at least three characters.")
        is_valid = False

        # date validator
        if len(form_data["date_column"]) == 0:
            flash("Please enter date_column.")
            is_valid = False
        else:
            try:
                datetime.strptime(form_data["date_column"], "%Y-%m-%d")
            except:
                flash("Invalid date_column.")
                is_valid = False

                # radio button validator
                if "radio_column" not in form_data:
                    flash("Please enter radio_column.")
                    is_valid = False
                elif form_data["radio_column"] not in ["choice1, choice2"]:
                    flash("radio_column must be at least three characters.")
                    is_valid = False

                return is_valid

    @classmethod
    def find_all(cls):
        """Finds all gizmos in the database."""

        query = "SELECT * FROM gizmos;"
        list_of_dicts = connectToMySQL(Gizmo.DB).query_db(query)

        gizmos = []
        for each_dict in list_of_dicts:
            gizmo = Gizmo(each_dict)
            gizmos.append(gizmo)
        return gizmos

    @classmethod
    def find_all_with_users(cls):
        """Finds all gizmos with users in the database"""

        query = """
        SELECT * FROM gizmos
        JOIN users
        ON gizmos.user_id = users.id;
        """
        list_of_dicts = connectToMySQL(Gizmo.DB).query_db(query)

        gizmos = []
        for each_dict in list_of_dicts:
            gizmo = Gizmo(each_dict)
            user_data = {
                "id": each_dict["gizmos.id"],
                "first_naem": each_dict["first_name"],
                "last_name": each_dict["last_name"],
                "email": each_dict["email"],
                "password": each_dict["password"],
                "created_at": each_dict["gizmos.created_at"],
                "updated_at": each_dict["gizmos.updated_at"],
            }

            user = User(user_data)
