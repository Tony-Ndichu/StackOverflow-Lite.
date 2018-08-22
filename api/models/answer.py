"""

#app/api/models/answer.py
This is the answer model
"""
from datetime import datetime
from ..database.connect import conn, cur


class AnswerModel():
    """handles operations for the answers"""

    def __init__(self, answer):
        self.answer = answer
        self.answer_date = datetime.now()

    def make_answer_dict(self, id_num, questionid):
        """receives answer object and turns it to dict"""
        return dict(
            answer=self.answer,
            answer_id=id_num,
            answer_date=self.answer_date,
            question_id=questionid,
            votes=0,
            accept_status=False,
            date_accepted=None,
        )

    def save_answer(user_id, question_id, answer_body):
        """save new qestion"""

        data = dict(userid=user_id, questionid=question_id,
                    answerbody=answer_body)

        submit = cur.execute("""INSERT INTO answers(user_id, question_id, answer_body, accepted , created_at) VALUES 
                    (%(userid)s, %(questionid)s, %(answerbody)s, false, current_timestamp )""", data)

        conn.commit()

        return "Successfully added answer"

    def confirm_que_poster(current_user_id, question_id):
        """confirm that the user trying to accept an answer actually posted the question"""

        fetch_question = "SELECT * FROM questions WHERE id = %s;"
        fetched_question = cur.execute(fetch_question, [question_id])
        result = cur.fetchall()

        for i in result:
            if i[1] != current_user_id:
                return "Sorry, you can't accept this answer since you didnt post the original question"

    def check_if_already_accepted(answer_id):
        """check if user already accepted the answers"""

        fetch_question = "SELECT * FROM answers WHERE id = %s;"
        fetched_question = cur.execute(fetch_question, [answer_id])
        result = cur.fetchall()

        for i in result:
            if i[4] == 'true':
                return "You have already accepted this answer"

    def accept_answer(answer_id):
        """accepts and answeer"""

        update_que = "UPDATE answers SET accepted = true WHERE id = %s;"
        cur.execute(update_que, [answer_id])
        conn.commit()

        return "Successfully accepted answer"
