import sqlite3

class Database :
    def __init__(self):
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()


    def get_tasks(self) :
        query = "SELECT * FROM alarms"
        result = self.cursor.execute(query)

        times = result.fetchall()
        return times
    
    def add_new_alarm(self , time) :

        try :
            query = f"INSERT INTO alarms VALUES('{time}')"
            self.cursor.execute(query)
            self.con.commit()
            return True 
        except :
            return False
        
    def remove_task(self , time) :
        try :
            query = "DELETE FROM alarms WHERE time = ? "
            self.cursor.execute(query ,(time,))
            self.con.commit()
            return True 
        
        except :
            return False

    def edit_task(self , oldTime , newTime) :
        try :
            query = f"UPDATE alarms SET time = '{newTime}' WHERE time = '{oldTime}' "
            self.cursor.execute(query)
            self.con.commit()
            return True 
        
        except :
            return False
