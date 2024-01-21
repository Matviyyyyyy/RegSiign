import sqlite3


class SQLAgent:
    def __init__(self, name_db):
        self.db = sqlite3.connect(name_db)
        self.create_tables()
        self.create_tables()

    def create_tables(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS SignUsers (        
            id_user INTEGER PRIMARY KEY,
            name_user TEXT,
            password_user TEXT,
            img_user TEXT,
           )

        ''')
        self.db.commit()


    def add_user(self, name_user, password_user, img_user):
        cursor = self.db.cursor()
        cursor.execute('INSERT INTO  SignUsers(name_user, password_user, img_user) VALUES(?, ?, ?, ?)', [name_user, password_user, img_user])
        cursor.close()
        self.db.commit()
    def get_correct_user(self):
        cursor = self.db.cursor()
        query = "SELECT * FROM SignUsers  WHERE name_user = ? AND password_user = ?"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        if len(result) > 1:
            return result
