from abc import ABC, abstractmethod

__all__ = ['User', 'Post']


class Model(ABC):
    @abstractmethod
    def parse(self, description) -> None:
        pass

    @abstractmethod
    def get_sql_insert(self) -> str:
        pass


class User(Model):
    def __init__(self, columns: tuple | None = None) -> None:
        super().__init__()

        self.id = None
        self.username = None
        self.name = None
        self.bio = None

        if columns is not None:
            self.parse(columns)

    def parse(self, columns: tuple) -> None:
        self.id, self.username, self.name, self.bio = columns

    def get_sql_insert(self) -> str:
        return f"""INSERT INTO users (username, name, bio) VALUES ('{self.username}', '{self.name}', '{self.bio}')"""


class Post(Model):
    def __init__(self, columns: tuple | None = None) -> None:

        super().__init__()

        self.id = None
        self.user_id = None
        self.tittle = None
        self.content = None

        if columns is not None:
            self.parse(columns)

    def parse(self, columns: tuple) -> None:
        self.id, self.user_id, self.tittle, self.content = columns

    def get_sql_insert(self) -> str:
        return f"""INSERT INTO posts (user_id, tittle, content) VALUES ({self.user_id}, '{self.tittle}', '{self.content}')"""