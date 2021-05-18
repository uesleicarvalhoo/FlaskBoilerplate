from typing import Dict, List

from src.ext.database import db


class BaseModel(db.Model):
    __abstract__ = True

    @staticmethod
    def create(**kwargs) -> "BaseModel":
        raise NotImplementedError

    @staticmethod
    def get(**kwargs) -> "BaseModel":
        raise NotImplementedError

    @staticmethod
    def get_all(**kwargs) -> List["BaseModel"]:
        raise NotImplementedError

    @classmethod
    def delete(cls) -> None:
        db.session.delete(cls)

    @classmethod
    def save(cls) -> None:
        db.session.add(cls)

    @classmethod
    def to_dict(cls) -> Dict:
        # TODO: Implementar a recorrencia
        return {key: value for key, value in cls.__mapper__.items()}
