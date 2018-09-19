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

    def turn_to_question_dict(list):
        question_list=[]

        for item in list:
            question_dict = dict(question_id=item[0], user_id = item[1], user_name = item[4] , title = item[2], description = item[3], no_of_answers = item[5] )
            question_list.append(question_dict)

        return question_list

    def get_questions(*args):

        question_list = []

        if args is not None:
            for current_user_id in args:
                fetch_user_questions = """SELECT Q.id, Q.user_id, Q.title, Q.description, U.username,
                                             (SELECT COUNT(A.question_id) FROM answers A WHERE A.question_id = Q.id) as answercount
                                             FROM QUESTIONS Q
                                             INNER JOIN users U ON Q.user_id = U.id
                                            WHERE Q.user_id = %s
                                                ORDER BY Q.id DESC
                                                ;"""

                fetched_questions = cur.execute(
                    fetch_user_questions, [current_user_id])
                result = cur.fetchall()


        que = cur.execute("""SELECT Q.id, Q.user_id, Q.title, Q.description, U.username,
             (SELECT COUNT(A.question_id) FROM answers A WHERE A.question_id = Q.id) as answercount
             FROM QUESTIONS Q
             INNER JOIN users U ON Q.user_id = U.id
             ORDER BY Q.id DESC
             ;""")

        try:
            que
        except (Exception, psycopg2.DatabaseError) as error:
            print (error)
            conn
            cur

        result = cur.fetchall()
        print(result)



        for i in result:
            question_list.append(i)

        return question_list

    def get_user_questions(current_user_id):

        question_list = []

        fetch_user_questions = """SELECT Q.id, Q.user_id, Q.title, Q.description, U.username,
                                             (SELECT COUNT(A.question_id) FROM answers A WHERE A.question_id = Q.id) as answercount
                                             FROM QUESTIONS Q
                                             INNER JOIN users U ON Q.user_id = U.id
                                            WHERE Q.user_id = %s
                                                ORDER BY Q.id DESC
                                                ;"""
        fetched_questions = cur.execute(
            fetch_user_questions, [current_user_id])
        result = cur.fetchall()

        for i in result:
            question_list.append(i)

        return question_list

    def save_to_db(self):
        """save new qestion"""

        data = dict(userid=self.user_id, title=self.title,
                    descr=self.description)

        submit = cur.execute("""INSERT INTO questions (user_id, title, description) VALUES 
                    (%(userid)s, %(title)s, %(descr)s)""", data)

        conn.commit()

        return "Successfully added question"

    def delete_question_and_its_answers(queid):
        """Delete a question"""

        delete_que = "DELETE FROM questions WHERE id = %s;"
        delete_answers ="DELETE FROM answers WHERE question_id = %s"
        cur.execute(delete_que, [queid])
        cur.execute(delete_answers, [queid])
        conn.commit()

    def check_who_posted(current_user_id, questionid):
        print(current_user_id)
        fetch_question = "SELECT * FROM questions WHERE id = %s and user_id = %s"
        fetched_question = cur.execute(fetch_question, [questionid, current_user_id])
        result = cur.fetchall()

        if not result:
            return "Sorry, you can't delete this question, only owner has permission"

    def most_answered(current_user_id):

        final_result = []

        fetch_question = """SELECT Q.id, Q.user_id, Q.title, Q.description, U.username,
                                             (SELECT COUNT(A.question_id) FROM answers A WHERE A.question_id = Q.id) as answercount
                                             FROM QUESTIONS Q
                                             INNER JOIN users U ON Q.user_id = U.id
                                             INNER JOIN answers A ON A.question_id = Q.id
                                             WHERE Q.user_id = %s
                                             GROUP BY A.question_id ,Q.id, U.username
                                              ORDER BY answercount DESC                                                     
                                                ;"""

        fetched_question = cur.execute(fetch_question, [current_user_id])
        que_result = cur.fetchall()

        if not que_result:
            return { "message" : "Sorry, none of your questions have any answers at the moment"}

        for i in que_result:
            final_result.append(dict(question_id=i[0], user_id = i[1], no_of_answers=i[5],
                                    title=i[2], description=i[3]))

        return final_result


    def get_user_answers(current_user_id):

        final_result = []

        fetch_question = """SELECT Q.id, Q.user_id, Q.title, Q.description, U.username,
                                             (SELECT COUNT(A.question_id) FROM answers A WHERE A.question_id = Q.id) as answercount
                                             FROM QUESTIONS Q
                                             INNER JOIN users U ON Q.user_id = U.id
                                             INNER JOIN answers A ON A.question_id = Q.id
                                             WHERE Q.user_id = %s
                                             GROUP BY A.question_id ,Q.id, U.username
                                              ORDER BY answercount DESC                                                     
                                                ;"""

        fetched_question = cur.execute(fetch_question, [current_user_id])
        que_result = cur.fetchall()

        if not que_result:
            return { "message" : "Sorry, none of your questions have any answers at the moment"}