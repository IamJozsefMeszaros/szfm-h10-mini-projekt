import os
import secrets

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(
        host = '0.0.0.0',
        port = 8080,
        threaded = True
        debug = True
    )