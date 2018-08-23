import psycopg2
import os

conn_string = os.getenv("DB_URL")
conn = psycopg2.connect(conn_string)
cur = conn.cursor()

