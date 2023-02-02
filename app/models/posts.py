from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy import func

from app.config.db import database


class Posts(database):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    created = Column(DateTime, server_default=func.now())
    title = Column(String)
    content = Column(String)