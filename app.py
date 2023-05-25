from flask import Flask

# Here it must go the configuration and setup code of the application e.g. databases connection, secret keys, etc.

app = Flask(__name__)

# importing routes. It's imported here to avoid circular dependency
from routes import *
