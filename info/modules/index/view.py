from flask import render_template
from . import index_blu


@index_blu.route('/')
def hello_world():
    return render_template('news/index.html')