import json
from abc import abstractmethod

from flask_login import UserMixin
from sqlalchemy import event
from werkzeug.security import generate_password_hash

from src.ext.database import db
from src.ext.database.models.base import BaseModel
from src.utils.exceptions import DataNotFoundError


class User(UserMixin, BaseModel):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True, nullable=False)
    username = db.Column("username", db.String(255), nullable=False, unique=True)
    password = db.Column("password", db.String(255), nullable=False)

    def create(**kwargs) -> "User":
        return User(id=kwargs["id"], username=kwargs["username"], password=kwargs["password"])

    @abstractmethod
    def get(**kwargs) -> "User":
        if user := User.query.filter_by(**kwargs).first():
            return user

        raise DataNotFoundError(f'No found user with args: "{json.dumps(kwargs)}"')


@event.listens_for(User.password, 'set', retval=True)
def hash_user_password(target, value, oldvalue, initiator):
    if value != oldvalue:
        return generate_password_hash(value)

    return value
