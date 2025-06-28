import sqlite3

class Database :
    def __init__(self):
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()


    def get_tasks(self) :
        query = "SELECT * FROM tasks ORDER BY is_done ASC, Priority ASC , id DESC"
        result = self.cursor.execute(query)

        tasks = result.fetchall()
        return tasks
    
    def add_new_task(self , title , discription , date) :

        try :
            self.cursor.execute("INSERT INTO tasks(title, description , DateTime) VALUES( ? , ? , ? )",(title, discription, date))
            self.con.commit()
            return True 
        
        except :
            return False
        
    def remove_task(self , title) :
        try :
            query = f"DELETE FROM tasks WHERE title = '{title}' "
            self.cursor.execute(query)
            self.con.commit()
            return True 
        
        except :
            return False

    def update_task(self , title) :
        try :
            query = f"UPDATE tasks SET is_done = 1 WHERE title = '{title}' "
            self.cursor.execute(query)
            self.con.commit()
            return True 
        
        except :
            return False
