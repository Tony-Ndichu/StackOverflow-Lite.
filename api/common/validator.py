"""

# app/api/common/validator.py
This module contains all the cide used to validate input
It is used by both the question and answer views and models
"""
import psycopg2
from ..database.connect import conn, cur


def check_if_already_exists(list_name, title):
    """"
    check if the question title or description
    already exists in storage
    """

    for item in list_name:
        if item['title'] == title:
            return 'Sorry, This title has already been used in another question'



def check_for_answer(answer):
    """check if a similar answer exists"""
    answer_list = []
    conn
    que = cur.execute("SELECT * FROM answers")

    try:
        que
    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
        conn
        cur

    result = cur.fetchall()    

    for item in result:
        if item[3] == answer:
            return True


def question_verification(title, description):
    """

    check the quality of questions sent such as 
    the length of the input and character type
    """
    if len(title) < 1:
        return 'You cannot post an empty title, Please add a title'
    if len(description) < 1:
        return 'You cannot post an empty description, Please add a description'
    if title.isdigit():
        return 'You cannot post a title with digits only, Please describe with some words'
    if description.isdigit():
        return 'You cannot post a description with digits only, Please describe with some words'


def check_using_id(list_name, other_id):
    """use the relevant id to find item in a list"""

    my_item = next((item for item in list_name if item[
                   'question_id'] == other_id), None)

    if my_item:
        return my_item
    return False


def check_quality(item):
    """check answer quality"""

    if len(item) < 1:
        return 'Too Short, Please add more input'


def find_answers_to_a_question(list_name, question_id):
    """find all the answers posted to a question"""

    my_items = [element for element in list_name if element[
        'question_id'] == question_id]

    if my_items:
        return my_items
    return False


def check_if_user_exists(user_list, username, email):
    """check if the username or email has already been used"""

    for item in user_list:
        if item[3] == username:
            return 'Sorry, This username has already been taken'
        if item[4] == email:
            return 'Sorry, This email is already in use'


def user_detail_verification(firstname, lastname, username):
    """check if details inputed are of a valid type"""
    if len(firstname) < 1 or len(lastname) < 1 or len(username) < 1:
        return 'Too short, please add more characters'
    if len(firstname) > 15 or len(lastname) > 15 or len(username) > 15:
        return 'Too long, please remove some characters'
    if firstname.isdigit() or lastname.isdigit() or lastname.isdigit():
        return 'This cannot be digits'
