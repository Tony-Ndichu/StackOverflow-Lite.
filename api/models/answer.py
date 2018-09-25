"""

#app/api/models/answer.py
This is the answer model
"""
from ..database.connect import conn, cur
import json
import datetime


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

    def accept_answer(question_id, answer_id):
        """accepts an answer"""
        unaccept_all = "UPDATE answers SET accepted = false WHERE question_id = %s";
        cur.execute(unaccept_all, [question_id])
        conn.commit()
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

    def get_que_answers(current_user_id, question_id):
        X = 0
        Y = 2
        user_id = current_user_id
       
        print(current_user_id)
        fetch_question = """SELECT A.id, A.user_id, A.question_id, A.answer_body, A.accepted, U.username,
            (SELECT COUNT(X.id) FROM upvotes X WHERE X.answer_id = A.id) as upvotes,
            (SELECT COUNT(Y.id) FROM downvotes Y WHERE Y.answer_id = A.id) as downvotes,
            (SELECT COUNT(X.id) FROM upvotes X WHERE X.answer_id = A.id and X.user_id = %s) as already_upvoted,
            (SELECT COUNT(Y.id) FROM downvotes Y WHERE Y.answer_id = A.id and Y.user_id = %s) as already_downvoted,
            A.created_at
                 FROM answers A 
                 INNER JOIN users U ON A.user_id = U.id WHERE A.question_id = %s
                 ORDER BY A.created_at DESC ;"""

        fetched_question = cur.execute(fetch_question, [user_id, user_id, question_id])
        result = cur.fetchall()

        answer_list = []
        for i in result:
            answer_list.append(dict(answer_id=i[0], user_id=i[1], user_name = i[5], question_id=i[2], answer_body=i[3], accepted=i[4], upvotes=i[6], downvotes=i[7],  upvote_id = X + 1,  downvote_id = Y + 1, already_upvoted = i[8], already_downvoted = i[9], time = AnswerModel.myconverter(time = i[10])))
            X += 1
            Y += 1
        return answer_list


    def myconverter(time=False):
        """
        Get a datetime object or a int() Epoch timestamp and return a
        pretty string like 'an hour ago', 'Yesterday', '3 months ago',
        'just now', etc
        """
        from datetime import datetime
        now = datetime.now()
        if type(time) is int:
            diff = now - datetime.fromtimestamp(time)
        elif isinstance(time,datetime):
            diff = now - time
        elif not time:
            diff = now - now
        second_diff = diff.seconds
        day_diff = diff.days

        if day_diff < 0:
            return ''

        if day_diff == 0:
            if second_diff < 10:
                return "just now"
            if second_diff < 60:
                return str(second_diff) + " seconds ago"
            if second_diff < 120:
                return "a minute ago"
            if second_diff < 3600:
                return str(int(round(second_diff / 60))) + " minutes ago"
            if second_diff < 7200:
                return "an hour ago"
            if second_diff < 86400:
                return str(int(round(second_diff / 3600))) + " hours ago"
        if day_diff == 1:
            return "Yesterday"
        if day_diff < 7:
            return str(day_diff) + " days ago"
        if day_diff < 31:
            return str(day_diff / 7) + " weeks ago"
        if day_diff < 365:
            return str(day_diff / 30) + " months ago"
        return str(day_diff / 365) + " years ago"