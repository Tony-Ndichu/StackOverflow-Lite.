"""

#app/api/models/comment.py
This is the comment model
"""
from datetime import datetime
from ..database.connect import conn, cur


class CommentModel():
    """handles operations for the answers"""
    def save_comment(res):
        """save new answer"""

        submit = cur.execute("""INSERT INTO comments(user_id, answer_id, comment_body, created_at) VALUES 
                    (%(arg1)s, %(arg2)s, %(arg3)s, current_timestamp )""", res)

        conn.commit()

        return "Successfully added Comment"

