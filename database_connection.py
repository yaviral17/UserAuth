import mysql.connector


from UserModel import User 

class MySQLDatabaseConnection:

    def get_connection(self):
        CNX = mysql.connector.connect(user = 'root', password = 'aviral05yadav', host = 'localhost')
        return CNX
    
    def CreateDatabase(self):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS users;")
        cursor.execute("USE users;")
        # create table with auto increament id
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, uid VARCHAR(255), name VARCHAR(255), email VARCHAR(255), phone VARCHAR(255), password VARCHAR(255));")
        CNX.commit()
        CNX.close()


    def createUser(self, user):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute(f"insert into users (uid, name, email, phone, password) values ('{user.uid}', '{user.name}', '{user.email}', '{user.phone}', '{user.password}');")
        CNX.commit()
        CNX.close()

    def getUser(self, email):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute("SELECT * FROM users WHERE email = %s;", (email,))
        result = cursor.fetchone()
        CNX.close()
        return result
    
    def getUserById(self, id):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute("SELECT * FROM users WHERE id = %s;", (id,))
        result = cursor.fetchone()
        CNX.close()
        return result
    
    def updateUser(self, user):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute("UPDATE users SET name = %s, email = %s, phone = %s, password = %s WHERE id = %s;", (user.name, user.email, user.phone, user.password, user.uid))
        CNX.commit()
        CNX.close()

    def deleteUser(self, id):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute("DELETE FROM users WHERE id = %s;", (id,))
        CNX.commit()
        CNX.close()

    def getAllUsers(self): 
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute("SELECT * FROM users;")
        result = cursor.fetchall()
        CNX.close()
        return result
    
    def deleteAllUsers(self):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute("DELETE FROM users;")
        CNX.commit()
        CNX.close()


    def getUserByUid(self, uid):
        CNX = self.get_connection()
        cursor = CNX.cursor()
        cursor.execute("USE users;")
        cursor.execute("SELECT * FROM users WHERE uid = %s;", (uid,))
        result = cursor.fetchone()
        CNX.close()
        return result
    
    def tupleToUser(self, tup):
        return User(tup[1], tup[2], tup[3], tup[4], tup[5])
    
    def listOfTupleToListOfUser(self, listOfTup):
        return [self.tupleToUser(tup) for tup in listOfTup]



if __name__ == "__main__":
    db = MySQLDatabaseConnection()
    # db.CreateDatabase()
    # db.deleteAllUsers()
    print(User.users_to_dict(db.listOfTupleToListOfUser(db.getAllUsers())))
    # print(db.tupleToUser( db.getUserByUid("oioaus")).to_dict())
    # db.createUser(User("oioaus","Aviral Yadav", "aviral05yadav@gmail","8077963037", "aviral05yadav"))
    # db.getAllUsers()