# Import Dependencies
from flask import Flask

# Create a new Flask app instance. " Instance" is a terrm in programming to refer to a singular version of something
app = Flask(__name__)

# Create Flask routes. the ('/') is always used as the starting point or root
@app.route('/')
# Create a function called hello_world()
def hello_world():
    return 'Hello world'

    