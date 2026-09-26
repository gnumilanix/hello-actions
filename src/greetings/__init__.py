from flask import Flask

app = Flask(__name__)

from greetings import routes
