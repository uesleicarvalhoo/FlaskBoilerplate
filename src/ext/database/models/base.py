from datetime import date, datetime, time
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
        pass

    @classmethod
    def to_json(cls) -> Dict:
        data = cls.to_dict()

        for col, value in data.items():
            if isinstance(value, datetime) or isinstance(value, date) or isinstance(value, time):
                data[col] = value.isoformat()
            elif isinstance(value, list):
                data[col] = [obj.to_json() if isinstance(obj, BaseModel) else obj for obj in value]
            elif isinstance(value, BaseModel):
                data[col] = value.to_json()

        return data
