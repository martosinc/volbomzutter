import psycopg2

conn = psycopg2.connect(
    host='192.168.1.75', user='user', dbname='db', password='123')

cursor = conn.cursor()

try:
    cursor.execute('DROP TABLE users;')
    cursor.execute('DROP TABLE posts;')
    conn.commit()

    print('Tables are droped')
except:
    conn.rollback()

user_table = """CREATE TABLE users 
(
id SERIAL PRIMARY KEY,
username VARCHAR(255),
name VARCHAR(255),
bio TEXT
);
"""

post_table = """CREATE TABLE posts 
(
id SERIAL PRIMARY KEY,
user_id INT,
tittle VARCHAR(255),
content TEXT
);
"""


cursor.execute(user_table)
cursor.execute(post_table)

conn.commit()

print('Tables are created')