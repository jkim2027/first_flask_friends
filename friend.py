from mysqlconnection import connectToMySQL

class Friend:
    DB = "first_flask"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    #CREATE
    @classmethod
    def save(cls, data):
        query = """INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)
                VALUES (%(fname)s, %(lname)s, %(occ)s, NOW(), NOW());"""
        return connectToMySQL(cls.DB).query_db(query, data)
    
    #READ
    @classmethod
    def get_all(cls): #retrieves all rows of the table
        query = "SELECT * FROM friends;"
        results = connectToMySQL(cls.DB).query_db(query)
        friends = []
        for friend in results:
            friends.append (cls(friend))
        return friends
    
    @classmethod
    def get_one(cls, friend_id): #retrieves one row of the table
        query = "SELECT * FROM friends WHERE id = %(id)s;"
        data = {'id': friend_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    # UPDATE
    @classmethod
    def update(cls, data):
        query = """
                UPDATE friends 
                SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s
                WHERE id = %(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    # DELETE
    @classmethod
    def delete(cls, friend_id):
        query = """
                DELETE FROM friends
                WHERE id = %(id)s;
                """
        data = {"id": friend_id}
        return connectToMySQL(cls.DB).query_db(query, data)