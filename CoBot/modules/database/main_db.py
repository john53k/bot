import psycopg2

from mysql.connector.errors import IntegrityError


db = psycopg2.connect("postgresql://mmuditon:ARmWeoQ_hNF27xYBp41CKieSLu7tnXP3@tiny.db.elephantsql.com/mmuditon")
cursor = db.cursor()


def create_table():
    cursor.execute("""CREATE TABLE IF NOT EXISTS last_client  (
                   user_id int,
                   last_sender int,
    )""")
    db.commit()


class OnStatus:
    
    def get_status(chat_id: int) -> bool:
        cursor.execute(f"SELECT status FROM working_status WHERE chat_id = {chat_id}")
        return bool(cursor.fetchone()[0])
    
    def update_status(chat_id: int, status: bool) -> None:
        cursor.execute(f"INSERT INTO working_status(chat_id, status) VALUES({chat_id}, {status})")
        db.commit()
        return "Status updated!"


class Last:


    def update_last_client(user_id: int):
        cursor.execute(f"UPDATE last_client SET user_id = {user_id}")
        db.commit()
    
    def update_last_sender(user_id: int):
        cursor.execute(f"UPDATE last_client SET last_sender = {user_id}")
        db.commit()

class Session:
    
    def new() -> str:
        try:
            cursor.execute("""INSERT INTO SessionDb(string_session) VALUES(1)""")
        except IntegrityError:
            return "Session already in database."
        else:
            return "Inserted in database successfully."
    
    def get():
        cursor.execute("SELECT string_session FROM SessionDb")
        return cursor.fetchall()