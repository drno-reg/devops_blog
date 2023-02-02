from sqlalchemy.orm import Session
import os

import app.models.posts as posts


def get_posts(db: Session):
    return db.query(posts.Posts).first()