from app import app, db
from app.models import User, Post

# from the app folder,import the app instance variable


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': Post, 'User': User}
