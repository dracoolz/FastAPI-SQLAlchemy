from sqlalchemy import Column, Integer, String, Boolean, DateTime
from database import Base
 
# AppUser
class AppUser(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    birth = Column(Integer)
    age = Column(Integer)
    gender = Column(String)
    quest_role = Column(Boolean)
    family = Column(String)
    last_login = Column(DateTime)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    publishedAt = Column(DateTime)

# Profile
class Profile(Base):
    __tablename__ = 'Profiles'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image = Column(String)
    content = Column(String)


# Families
class Family(Base):
    __tablename__ = 'Families'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)

# Post
class Post(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    user = Column(Integer)
    kids = Column(Integer)
    content = Column(String)
    image_url = Column(String)
    like = Column(Integer)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    publishedAt = Column(DateTime)

# Comment
class Comment(Base):
    __tablename__ = 'Comments'

    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer)
    post_id = Column(Integer)
    user_id = Column(Integer)
    content = Column(String)
    createdAt = Column(DateTime)


# Tree
class Tree(Base):
    __tablename__ = 'Trees'

    id = Column(Integer, primary_key=True)
    growth_stage = Column(Integer)
    quest = Column(Integer)
    watering = Column(DateTime)


# Quest types
class QuestType(Base):
    __tablename__ = 'QuestTypes'

    id = Column(Integer, primary_key=True)
    kinds = Column(String)
    online = Column(Boolean)


# Rewards
class Reward(Base):
    __tablename__ = 'Rewards'

    id = Column(Integer, primary_key=True)
    content = Column(String)


# Quest
class Quest(Base):
    __tablename__ = 'Quests'

    id = Column(Integer, primary_key=True)
    content = Column(Integer)
    quest_kinds = Column(String)
    completed = Column(Boolean)