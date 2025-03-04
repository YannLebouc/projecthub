from src import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional
import datetime


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    roles: Mapped[list[str]]
    created_at: Mapped[datetime.datetime]
    updated_at: Mapped[Optional[datetime.datetime]]
