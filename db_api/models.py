from abc import ABC, abstractmethod

__all__ = ['User', 'Post']


class Model(ABC):
    @abstractmethod
    def parse(self, description) -> None:
        pass

    @abstractmethod
    def get_sql_insert(self) -> str:
        pass

    @abstractmethod
    def get_sql_update(self) -> str:
        pass


class User(Model):
    def __init__(self, columns: tuple | None = None) -> None:
        super().__init__()

        self.id = None
        self.username = None
        self.name = None
        self.password_hash = None
        self.bio = None

        if columns is not None:
            self.parse(columns)

    def parse(self, columns: tuple) -> None:
        self.id, self.username, self.name, self.password_hash, self.bio = columns

    def get_sql_insert(self) -> str:
        return f"""INSERT INTO users (username, name, password_hash, bio) VALUES ('{self.username}', '{self.name}', '{self.password_hash}', '{self.bio}')"""

    def get_sql_update(self) -> str:
        return f"""
                UPDATE users SET 
                username = {self.username},
                name = {self.name},
                password_hash = {self.password_hash}, 
                bio = {self.bio}
                WHERE id = {self.id}
                """


class Post(Model):
    def __init__(self, columns: tuple | None = None) -> None:

        super().__init__()

        self.id = None
        self.user_id = None
        self.publication_timestamp = None
        self.title = None
        self.content = None

        if columns is not None:
            self.parse(columns)

    def parse(self, columns: tuple) -> None:
        self.id, self.user_id, self.publication_timestamp, self.title, self.content = columns

    def get_sql_insert(self) -> str:
        return f"""INSERT INTO posts (user_id, title, content) VALUES ({self.user_id}, '{self.title}', '{self.content}')"""

    def get_sql_update(self) -> str:
        return f"""
                UPDATE posts SET 
                tittle = {self.title},
                content = {self.content}
                WHERE id = {self.id}
                """
