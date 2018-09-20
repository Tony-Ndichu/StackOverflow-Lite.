"""
#app/api/models/user.py
This is the user model
"""
import psycopg2
from ..database.connect import conn, cur
from werkzeug.security import generate_password_hash, \
    check_password_hash


class UserModel():
    """this handles user registration and authentication"""

    def get_all_users():
        """retrieve all users from the database"""
        user_list = []
        conn
        que = cur.execute("SELECT * FROM users")

        try:
            que
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn
            cur

        result = cur.fetchall()

        for i in result:
            user_list.append(result)

        return result

    def get_profile(current_user_id):
        """retrieve a user's profile details"""
        user_profile = []

        fetch_profile = """SELECT U.id, U.first_name, U.last_name, U.username, U.email,
                                             (SELECT COUNT(Q.id) FROM questions Q WHERE Q.user_id = U.id) as questioncount,
                                             (SELECT COUNT(A.id) FROM answers A WHERE A.user_id = U.id) as answercount
                                             FROM users U
                                            WHERE U.id = %s
                                                ;"""

        fetched_profile = cur.execute(fetch_profile, [current_user_id])
        result = cur.fetchall()

        for item in result:
            user_dict = dict(user_id=item[0], first_name = item[1], last_name = item[2] , username = item[3], email = item[4], no_of_questions = item[5], no_of_answers = item[6])
            user_profile.append(user_dict)

        return user_profile


    def create_user(first_name, last_name, username, email, password):
        """save new user data"""

        data = dict(first_name=first_name, last_name=last_name,
                    username=username, email=email, password=generate_password_hash(password))

        submit = cur.execute("""INSERT INTO users (first_name, last_name, username, email, password) VALUES 
					(%(first_name)s, %(last_name)s, %(username)s, %(email)s, %(password)s)""", data)

        conn.commit()

    def check_if_exists(username):
        """checks if user exists in system"""
        fetch_question = "SELECT * FROM users WHERE username = %s;"
        fetched_question = cur.execute(fetch_question, [username])
        result = cur.fetchall()

        return result

    def find_by_username(username, password):
        """check user dedtails on login"""
        user_list = []

        conn
        que = cur.execute("SELECT * FROM users")

        try:
            que
        except (Exception, psycopg2.DatabaseError) as error:
            conn
            cur
            que

        result = cur.fetchall()

        for i in result:

            if i[3] == username and check_password_hash(i[5], password):
                u_id = i[0]
                return u_id
