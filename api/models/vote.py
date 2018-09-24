"""

# app/api/models/vote.py
This is the answer model
"""
from ..database.connect import conn, cur


class VoteModel():
    """handles operations for the votes"""

    def upvote_answer(current_user_id, answer_id):
        """upvote answer"""

        data = dict(user_id=current_user_id, answerid=answer_id)

        upvote_answers = cur.execute("""INSERT INTO upvotes (user_id, answer_id) VALUES
    						(%(user_id)s, %(answerid)s) """, data)

        conn.commit()

        return True

    def check_if_upvoted(current_user_id, answer_id):
        """checks if the same upvote already exists"""

        que = "SELECT * FROM upvotes WHERE user_id = %s AND answer_id = %s;"
        run_que = cur.execute(que, [current_user_id, answer_id])
        result = cur.fetchall()

        if result:
            return True

    def remove_upvote(current_user_id, answer_id):
        """checks if the same upvote already exists and removes upvote"""

        que = "DELETE FROM upvotes WHERE user_id = %s AND answer_id = %s;"
        run_que = cur.execute(que, [current_user_id, answer_id])
        conn.commit()

    def count_upvotes(answer_id):
        """counts the number of upvotes"""
        count_list = []

        que = "SELECT COUNT(id) FROM upvotes WHERE answer_id = %s;"
        run_que = cur.execute(que, [answer_id])
        result = cur.fetchall()

        return result[0]

    def downvote_answer(current_user_id, answer_id):
        """downvote answer"""

        data = dict(user_id=current_user_id, answerid=answer_id)

        upvote_answers = cur.execute("""INSERT INTO downvotes (user_id, answer_id) VALUES 
    						(%(user_id)s, %(answerid)s) """, data)

        conn.commit()

        return True

    def remove_downvote(current_user_id, answer_id):
        """checks if the same downvote already exists and removes downvote"""

        que = "DELETE FROM downvotes WHERE user_id = %s AND answer_id = %s;"
        run_que = cur.execute(que, [current_user_id, answer_id])
        conn.commit()


    def check_if_downvoted(current_user_id, answer_id):
        """checks if the same downvote already exists"""

        que = "SELECT * FROM downvotes WHERE user_id = %s AND answer_id = %s;"
        run_que = cur.execute(que, [current_user_id, answer_id])
        result = cur.fetchall()

        if result:
            return True

    def count_downvotes(answer_id):
        """counts the number of downvotes"""
        count_list = []

        que = "SELECT COUNT(id) FROM downvotes WHERE answer_id = %s;"
        run_que = cur.execute(que, [answer_id])
        result = cur.fetchall()

        return result[0]
