from model import Model

__all__ = ['User']


class User(Model):
    def __init__(self, description: tuple | None = None) -> None:
        super().__init__()

        self.id = None
        self.username = None
        self.name = None
        self.location = None
        self.bio = None

        if description is not None:
            self.parse(description)

    def parse(self, description: tuple) -> None:
        self.id, self.username, self.name, self.location, self.bio = description

    def get_sql_insert(self) -> str:
        return f"""INSERT INTO users (username, name, location, bio) VALUES ({self.username}, {self.name}, {self.location}, {self.bio})"""
