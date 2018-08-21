from api.database.connect import conn, cur
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
          created_at timestamp NULL DEFAULT NULL 
        )
        """
    

    create_questions = """ CREATE TABLE IF NOT EXISTS questions (
            id int NOT NULL,
            user_id int NOT NULL,
            title varchar(255) UNIQUE NOT NULL,
            description varchar(255) UNIQUE NOT NULL,    
            created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            price varchar(200)  NOT NULL 
        )
        """

    create_answers = """CREATE TABLE IF NOT EXISTS answers (
            id int NOT NULL,
            question_id int NOT NULL,
            answer_body varchar(255) UNIQUE NOT NULL,
            created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            price varchar(200)  NOT NULL
        )
        """

    table_list= [create_users , create_questions , create_answers ]
        
    try:
        # create table one by one
        for table in table_list:
            cur.execute(table)
        # close communication with the PostgreSQL database server
        
        # commit the changes
        conn.commit()
        print("Created successfully")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
