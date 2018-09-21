"""

#app/api/models/answer.py
This is the answer model
"""
from ..database.connect import conn, cur


class AnswerModel():
    """handles operations for the answers"""

    def get_answers():

        answer_list = []

        # if args is not None:
        #     for questionid in args:
        #         fetch_user_answers = """SELECT A.id, A.user_id, A.question_id, A.answer_body, A.accepted
        #          FROM answers A 
        #          INNER JOIN users U ON A.user_id = U.id WHERE A.question_id = %s
        #          ORDER BY A.id DESC ;"""
        #         fetched_answers = cur.execute(fetch_user_answers, [questionid])
        #         result = cur.fetchall()


        que = cur.execute("""SELECT A.id, A.user_id, A.question_id, A.answer_body, A.accepted
                 FROM answers A 
                 INNER JOIN users U ON A.user_id = U.id
                 ORDER BY A.id DESC ;""")

        result = cur.fetchall()

        for i in result:
            answer_list.append(i)

        return answer_list


    def get_answers_to_specific_que(questionid):
        fetch_answers = """SELECT A.id, A.user_id, U.username, A.question_id, A.answer_body, A.accepted
                 FROM answers A 
                 INNER JOIN users U ON A.user_id = U.id WHERE A.question_id = %s
                 ORDER BY A.id DESC ;"""

        fetched_answers = cur.execute(fetch_answers, [questionid])
        result = cur.fetchall()

        answer_list = []
        for i in result:
            answer_list.append(i)

        return answer_list

    def save_answer(res):
        """save new answer"""

        submit = cur.execute("""INSERT INTO answers(user_id, question_id, answer_body, accepted ) VALUES 
                    (%(arg1)s, %(arg2)s, %(arg3)s, false )""", res)

        conn.commit()

        return "Success!! Your answer has been added"

    def check_who_posted(current_user_id, answer_id):

        fetch_question = "SELECT * FROM answers WHERE id = %s and user_id = %s"
        fetched_question = cur.execute(fetch_question, [answer_id, current_user_id])
        result = cur.fetchall()

        if not result:
            return True

    def check_if_already_accepted(answer_id):
        """check if user already accepted the answers"""

        fetch_question = "SELECT * FROM answers WHERE id = %s;"
        fetched_question = cur.execute(fetch_question, [answer_id])
        result = cur.fetchall()

        for i in result:
            if i[4] == 'true':
                return "You have already accepted this answer"

    def accept_answer(answer_id):
        """accepts an answer"""

        update_que = "UPDATE answers SET accepted = true WHERE id = %s;"
        cur.execute(update_que, [answer_id])
        conn.commit()

        return "Successfully accepted answer"

    def update_answer(answer_id, answer_body):
        """updates an answer"""

        update_que = "UPDATE answers SET answer_body = %s WHERE id = %s;"
        cur.execute(update_que, [answer_body, answer_id])
        conn.commit()

        return "Successfully updated answer"

    def get_que_answers(question_id):
        fetch_question = """SELECT A.id, A.user_id, A.question_id, A.answer_body, A.accepted, U.username
                 FROM answers A 
                 INNER JOIN users U ON A.user_id = U.id WHERE A.question_id = %s
                 ORDER BY A.id DESC ;"""

        fetched_question = cur.execute(fetch_question, [question_id])
        result = cur.fetchall()

        answer_list = []
        for i in result:
            answer_list.append(dict(answer_id=i[0], user_id=i[1], user_name = i[5], question_id=i[2], answer_body=i[3], accepted=i[4]))

        return answer_list