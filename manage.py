from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from info import create_app,db


app = create_app('development')
manger = Manager(app)
Migrate(app,db)
manger.add_command('db',MigrateCommand)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    manger.run()