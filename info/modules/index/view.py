from flask import render_template

from info import redis_store
from . import index_blu


@index_blu.route('/')
def hello_world():
    redis_store.set('name','laowang')
    return render_template('news/index.html')