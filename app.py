import os, secrets

from flask import (Flask,
                   render_template,
                   request,
                   redirect,
                   url_for,
                   jsonify)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('level')
    return redirect(url_for('level_page', level=data))

@app.route('/level/<int:level>')
def level_page(level: int):
    try:
        if level in range(1,4):
            return render_template('quiz.html', level=level)
        else:
            raise ValueError("Invalid value...")
    except:
        return jsonify({"error": "Invalid value..."}), 400

if __name__ == "__main__":
    app.run(
        host = '0.0.0.0',
        port = 8080,
        threaded = True,
        debug = True
    )