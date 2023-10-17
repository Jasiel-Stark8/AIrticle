from flask import Flask, render_template, request
from models import article
from models import autosave
from models import user
from api.v1 import articles
from api.v1 import auth
from api.v1 import autosave

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return "Serving Page"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
