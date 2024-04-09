'''Configuration of flask project'''

from flask import Flask, render_template

#assigning FLASK session
app = Flask(__name__)

@app.route('/')
def index():
    return /0

if __name__ == '__main__':
    app.run(debug=True)
