import psycopg2

conn = psycopg2.connect(
    host='127.0.0.1', user='user', dbname='db', password='123')

cursor = conn.cursor()

try:
    cursor.execute('DROP TABLE users;')
    cursor.execute('DROP TABLE posts;')
    conn.commit()

    print('Tables are droped')
except:
    conn.rollback()

user_table = """
CREATE TABLE users 
(
id SERIAL,
username VARCHAR(255) PRIMARY KEY,
name VARCHAR(255),
password_hash TEXT,
bio TEXT
);
"""

post_table = """
CREATE TABLE posts 
(
id SERIAL PRIMARY KEY,
user_id INT,
publication_timestamp TIMESTAMP NOT NULL DEFAULT now(),
title VARCHAR(255),
content TEXT
);
"""


cursor.execute(user_table)
cursor.execute(post_table)

conn.commit()

print('Tables are created')