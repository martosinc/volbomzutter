import psycopg2

conn = psycopg2.connect(
    host='192.168.40.90', user='user', dbname='db', password='123')

cursor = conn.cursor()


user_table = """CREATE TABLE users (
id INT PRIMARY KEY,
usernmae VARCHAR(255),
name VARCHAR(255),
location VARCHAR(255),
bio TEXT
);
"""

post_table = """CREATE TABLE posts (
id INT PRIMARY KEY,
user_id INT,
tittle VARCHAR(255),
content TEXT
);
"""


cursor.execute(user_table)
cursor.execute(post_table)

conn.commit()