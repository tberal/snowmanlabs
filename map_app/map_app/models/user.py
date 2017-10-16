from datetime import datetime

from sqlalchemy import Column, String, DateTime

from map_app.models.base import Base

class User(Base):
    """
    Database model for the app users.

    Fields:
        id: String. The user's facebook ID.
        created: Datetime. Date when a given user was added to the database.
        updated: Datetime. Records the last change to an user entry.
        name: String. User's complete name provided by facebook
        profile_url: String. Facebook profile url
        access_token: String. Access token provided by facebook
    """
    __tablename__ = 'users'

    id = Column(String(1024), nullable=False, primary_key=True)
    created = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated = Column(DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)
    name = Column(String(1024), nullable=False)
    profile_url = Column(String(1024), nullable=False)
    access_token = Column(String(1024), nullable=False)
