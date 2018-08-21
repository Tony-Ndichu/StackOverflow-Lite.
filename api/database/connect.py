import psycopg2

conn_string = "host='localhost' dbname='stackoverflowlite' user='postgres' password='tony1234'"
conn = psycopg2.connect(conn_string)
cur = conn.cursor()