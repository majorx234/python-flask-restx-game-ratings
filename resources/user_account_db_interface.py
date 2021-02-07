import psycopg2


class UserAccountDBInterface():
    def __init__(self, db="gamewebsitedb", user="ros"):
        # konstruktor wird beim initialisieren aufegerufen
        self.connection = psycopg2.connect(database=db, user=user)
        self.cursor = self.connection.cursor()

    def loginQuery(self, user, password):
        query = "Select username FROM users WHERE username = '{}' AND password = '{}'; ".format(user, password)
        print("query = {}".format(query))
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        result_user =  records[0][0]
        if (result_user == user):
            return True
        else:
            return False

    def close(self):
        self.cursor.close()
        self.connection.close()      
