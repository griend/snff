from flask import Flask
from views import views

app = Flask(__name__, instance_relative_config=True)
app.register_blueprint(views)
