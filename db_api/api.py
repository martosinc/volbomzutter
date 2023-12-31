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

    def update_user(self, user: User):
        self.cursor.execute(user.get_sql_update)

        self.conn.commit()

    def add_post(self, post: Post):
        self.cursor.execute(post.get_sql_insert())

        self.conn.commit()

    def update_post(self, post: Post):
        self.cursor.execute(post.get_sql_update())

        self.conn.commit()

    def delete_post(self, post: Post):
        self.cursor.execute('DELETE FROM posts where id = %s', (post.id))

        self.conn.commit()

    def delete_post_by_id(self, id: int):
        self.cursor.execute('DELETE FROM posts where id = %s', (id, ))

        self.conn.commit()

    def get_user_by_id(self, id: int) -> User | None:
        self.cursor.execute('SELECT * FROM users WHERE id = %s', (id, ))

        return User(self.cursor.fetchone())

    def get_user_by_username(self, username: str) -> User | None:
        self.cursor.execute(
            'SELECT * FROM users WHERE username = %s', (username, ))
        user_data = self.cursor.fetchone()

        if user_data is None: return None

        return User(user_data)

    def get_post_by_id(self, id: int) -> Post | None:
        self.cursor.execute('SELECT * FROM posts WHERE id = %s', (id, ))

        return Post(self.cursor.fetchone())

    def get_posts_by_user(self, user: User):
        self.cursor.execute(
            'SELECT * FROM posts WHERE user_id = %s', (user.id, ))

        return [Post(row) for row in self.cursor.fetchall()]

    def get_posts(self, limit: int = -1) -> list[Post] | None:
        if limit < 0:
            self.cursor.execute(
                'SELECT * FROM posts ORDER BY publication_timestamp')
        else:
            self.cursor.execute(
                'SELECT * FROM posts ORDER BY publication_timestamp LIMIT %s', (limit, ))

        return [Post(row) for row in self.cursor.fetchall()]

    def get_users(self, limit: int = -1) -> list[User] | None:
        if limit < 0:
            self.cursor.execute(
                'SELECT * FROM users')
        else:
            self.cursor.execute(
                'SELECT * FROM users LIMIT %s', (limit, ))

        return [User(row) for row in self.cursor.fetchall()]
