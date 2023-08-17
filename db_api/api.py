import psycopg2

from .models import User, Post

__all__ = ['API', 'User', 'Post']


class API:
    def __init__(self, host=None, user=None, db_name=None, password=None) -> None:
        self.conn = psycopg2.connect(
            host=host, user=user, dbname=db_name, password=password)

        self.cursor = self.conn.cursor()

    def add_user(self, user: User) -> None:
        self.cursor.execute(user.get_sql_insert())

        self.conn.commit()

    def add_post(self, post: Post):
        self.cursor.execute(post.get_sql_insert())

        self.conn.commit()

    def get_user(self, id: int) -> User | None:
        self.cursor.execute('SELECT * FROM users WHERE id = %d', (id, ))

        return User(self.cursor.fetchone())

    def get_post(self, id: int) -> Post | None:
        self.cursor.execute('SELECT * FROM posts WHERE id = %d', (id, ))

        return Post(self.cursor.fetchone())

    def get_posts_by_user(self, user: User):
        self.cursor.execute('SELECT * FROM posts WHERE id = %d', (user.id, ))

        return [Post(row) for row in self.cursor.fetchall()]

    def get_all_posts(self) -> list[Post] | None:
        self.cursor.execute('SELECT * FROM users')

        return [Post(row) for row in self.cursor.fetchall()]

api = API(host='', user='', db_name='', password='')

api.add_user(User((1, 'user', 'user', 'location', '404')))

print(api.get_user(1))