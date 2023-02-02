from flask import Flask, render_template
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import os, psycopg2

from app.config.db import database, engine
from app.models.posts import Posts

import json, jsonify

from werkzeug.exceptions import abort

Posts.metadata.create_all(bind=engine)

SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URI")


app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(SQLALCHEMY_DATABASE_URL)
    return conn


def get_post(post_id):
    conn = get_db_connection()
    cur = conn.cursor()
    sql = """
    SELECT * FROM posts WHERE id = %s;
    """ % post_id
    print(sql)
    cur.execute(sql)
    post = cur.fetchall()
    print(post)
    conn.close()
    if post is None:
        abort(404)
    return post


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM posts;')
    posts = cur.fetchall()
    cur.close()
    conn.close()
    print(posts)
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)
