import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    Firstname = Column(String(250), nullable=False)
    Lastname = Column(String(250), nullable=False)
    Email = Column(String)

class Follower(Base):
    __tablename__ = 'Follower'
    User_from_id = Column(Integer, ForeignKey(User.id),primary_key=True)
    User_to_id = Column(Integer, ForeignKey(User.id),primary_key=True)
    User = relationship(User)

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    User = relationship(User)

class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer, primary_key=True)
    Comment_text = Column(String(250), nullable=False)
    Author_id = Column(Integer, ForeignKey('User.id'))
    Post_id = Column(Integer, ForeignKey('Post.id'))
    User = relationship(User)
    Post = relationship(Post)

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    Post_id = Column(Integer, ForeignKey('Post.id'))
    Post = relationship(Post)    




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e