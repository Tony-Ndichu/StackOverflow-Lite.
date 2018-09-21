"""

#app/api/models/comment.py
This is the comment model
"""
from datetime import datetime
from ..database.connect import conn, cur


class CommentModel():
    """handles operations for the answers"""


    # def get_comments(*args):

    #     user_details=[]
    #     comment_list = []

    #     if args is not None:
    #         for commentid in args:
    #             fetch_user_comments = """SELECT C.id, C.user_id, C.answer_id, C.comment_body
    #              FROM comments C 
    #              INNER JOIN users U ON C.user_id = U.id WHERE C.answer_id = %s
    #              ORDER BY C.id DESC ;"""
    #             fetched_comments = cur.execute(fetch_user_comments, [questionid])
    #             result = cur.fetchall()


    #     que = cur.execute("""SELECT C.id, C.user_id, C.answer_id, C.comment_body
    #              FROM comments C 
    #              INNER JOIN users U ON C.user_id = U.id
    #              ORDER BY C.id DESC ;""")

    #     try:
    #         que
    #     except (Exception, psycopg2.DatabaseError) as error:
    #         print (error)
    #         conn
    #         cur

    #     result = cur.fetchall()


    #     for i in result:
    #         comment_list.append(i)

    #     return comment_list


    def save_comment(res):
        """save new answer"""

        submit = cur.execute("""INSERT INTO comments(user_id, answer_id, comment_body) VALUES 
                    (%(arg1)s, %(arg2)s, %(arg3)s)""", res)

        conn.commit()

        return "Successfully added Comment"

