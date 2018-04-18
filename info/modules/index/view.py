from . import index_blu


@index_blu.route('/')
def hello_world():
    return 'Hello World!'