from sqlalchemy import Text
from sqlalchemy.ext.hybrid import hybrid_property
from werkzeug.security import generate_password_hash
from graphene_boilerplate.ext import db


class User(db.Model):
    __tablename__ = "user"
    full_name = db.Column(Text, nullable=False)
    email = db.Column(Text, nullable=False, unique=True)
    items = db.relationship("Item", back_populates="user")

    _password = db.Column(Text, nullable=False)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter  # type: ignore
    def password(self, plaintext):
        self._password = generate_password_hash(plaintext)