from app.config import Config
from flask import  Flask
from .config import Config

app=Flask(__name__)
app.config.from_object(Config)

#shows path to static file
from app import route,models