from datetime import datetime

from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Text, 
    Boolean, 
    DateTime, 
    ForeignKey,
    func,
    PrimaryKeyConstraint,
)
from sqlalchemy.orm import (
    relationship,
    backref,
)
from .database import db


class User(db.Model):

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True, nullable=False)
    password = Column(String(32), nullable=False)

    def __str__(self) -> str:
        return f"User(id={self.id}, username={self.username!r}, age={self.age})"

    def __repr__(self) -> str:
        return f'From repr! {str(self)}'


class Post(db.Model):

    id = Column(Integer, primary_key=True)
    title = Column(String(32), unique=True, nullable=False)
    description = Column(Text, nullable=True)
    is_approved = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship(User, backref=backref("posts", lazy="dynamic"))


class Tag(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)


class PostTag(db.Model):

    __table_args__ = (
        PrimaryKeyConstraint('post_id', 'tag_id'),
    )
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tag.id'), nullable=False)


class Comment(db.Model):

    id = Column(Integer, primary_key=True)
    text = Column(String(32), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship(User, backref=backref("Comment", lazy="dynamic"))
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    user = relationship(User, backref=backref("Comment", lazy="dynamic"))