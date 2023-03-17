from flask import Flask
from api.index import app as application

# Create an instance of Flask for the serverless environment
server = Flask(__name__)

# Expose the Flask app as a serverless function
@server.route("/api/<username>")
def handler(username):
    return application.view_functions["get_rank"](username)
