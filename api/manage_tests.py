from .database.connect import conn2, cur2
import psycopg2


def create_tables():
    """ 
    create tables in the database
    """
    create_users = """ CREATE TABLE IF NOT EXISTS users (
          id bigserial NOT NULL PRIMARY KEY,
          first_name varchar(155) NOT NULL,
          last_name varchar(255) NOT NULL,
          username varchar(255) UNIQUE NOT NULL,
          email varchar(255) UNIQUE NOT NULL,
          password varchar(255) NOT NULL,
          created_at timestamp  
        )
        """
    

    create_questions = """ CREATE TABLE IF NOT EXISTS questions (
            id bigserial NOT NULL PRIMARY KEY,
            user_id int NOT NULL,
            title varchar(100) UNIQUE NOT NULL,
            description varchar(255) NOT NULL,    
            created_at timestamp
        )
        """

    create_answers = """CREATE TABLE IF NOT EXISTS answers (
            id bigserial NOT NULL PRIMARY KEY,
            user_id int NOT NULL,
            question_id int NOT NULL,
            answer_body varchar(255) UNIQUE NOT NULL,
            accepted varchar(255),
            created_at timestamp 
        )
        """

    table_list= [create_users , create_questions , create_answers ]
        
    try:
        # create table one by one
        for table in table_list:
            cur2.execute(table)
        # close communication with the PostgreSQL database server
        
        # commit the changes
        conn2.commit()
        print("Created successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

