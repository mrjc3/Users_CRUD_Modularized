from flask_app.config.mysqlconnection import connectToMySQL

class User:


    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_users(cls):

        query = "SELECT * FROM users"
        #displays in dict so must loop thru and add to a list
        results = connectToMySQL("users_schema").query_db(query)

        users = [User(row) for row in results]

        return users


    @classmethod
    def create_new(cls, data):

        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"

        result = connectToMySQL("users_schema").query_db(query, data)

        # this result returns an id for the new entry into the database
        return result



    @classmethod
    def get_one_user(cls, data):

        query = "SELECT * FROM users WHERE id = %(id)s;"

        result = connectToMySQL('users_schema').query_db(query, data)

        return result


    @classmethod
    def update_user(cls, data):

        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"

        result = connectToMySQL('users_schema').query_db(query, data)



    @classmethod
    def delete_user(cls, data):

        query = "DELETE FROM users WHERE id = %(id)s;"

        result = connectToMySQL('users_schema').query_db(query, data)
