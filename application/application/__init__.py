from flask import Flask
from application.users.views import users
app = Flask(__name__)

import application.models
import application.views

app.register_blueprint(users, url_prefix='/users')

    
if __name__ == "__main__":
    app.run()