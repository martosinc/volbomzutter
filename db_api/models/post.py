from model import Model

__all__ = ['Post']


class Post(Model):
    def __init__(self, description: tuple | None = None) -> None:

        super().__init__()

        self.id = None
        self.user_id = None
        self.tittle = None
        self.content = None

        if description is not None:
            self.parse(description)

    def parse(self, description: tuple) -> None:
        self.id, self.user_id, self.tittle, self.content = description

    def get_sql_insert(self) -> str:
        return f"""INSERT INTO posts (user_id, tittle, content) VALUES ({self.user_id}, {self.tittle}, {self.content})"""
