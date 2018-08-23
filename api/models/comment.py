"""

#app/api/models/comment.py
This is the comment model
"""
from datetime import datetime
from ..database.connect import conn, cur


class CommentModel():
    """handles operations for the answers"""
    def save_comment(user_id, answer_id, comment_body):
        """save new answer"""

        data = dict(userid=user_id, answerid=answer_id,
                    commentbody=comment_body)

        submit = cur.execute("""INSERT INTO comments(user_id, answer_id, comment_body, created_at) VALUES 
                    (%(userid)s, %(answerid)s, %(commentbody)s, current_timestamp )""", data)

        conn.commit()

        return "Successfully added Comment"

