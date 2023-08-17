from abc import ABC, abstractmethod

__all__ = ['Model']


class Model(ABC):
    @abstractmethod
    def parse(self, description) -> None:
        pass

    @abstractmethod
    def get_sql_insert(self) -> str:
        pass
