from src import db
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(Nullable=False, unique=True)
    password: Mapped[str] = mapped_column(Nullable=False)
    email: Mapped[str] = mapped_column(Nullable=False, unique=True)
    is_admin: Mapped[bool] = mapped_column(Nullable=False, default=False)
    is_active: Mapped[bool] = mapped_column(Nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        default=datetime.utcnow, onupdate=datetime.utcnow
    )

    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email

    def __repr__(self):
        return f"User id={self.id}, username={self.username}, email={self.email}, created_at={self.created_at}, is_active={self.is_active}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def set_to_admin(self):
        self.is_admin = True
