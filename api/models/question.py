""""

#app/api/models/question.py
This is the question model
"""
import psycopg2
from ..database.connect import conn, cur

class QuestionModel():
    """this class handles question-related operations"""

    def __init__(self, title, description, user_id):
        self.title = title
        self.description = description
        self.user_id = user_id

    def get_all_questions():
        """retrieve all users from the database"""
        question_list = []
        conn
        que = cur.execute("SELECT * FROM questions")

        try:
            que
        except (Exception, psycopg2.DatabaseError) as error:
            print (error)
            conn
            cur

        result = cur.fetchall()

        for i in result:
            question_list.append(result)

        return result

    def save_to_db(self):
        """save new qestion"""

        data = dict(userid = self.user_id, title=self.title, descr = self.description)

        submit = cur.execute("""INSERT INTO questions (user_id, title, description, created_at) VALUES 
                    (%(userid)s, %(title)s, %(descr)s, current_timestamp )""", data)

        conn.commit()

        return "Successfully added question"
