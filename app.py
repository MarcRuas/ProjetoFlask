from flask import Flask, render_template
from api.controller.produtos_controller import produtos_controller_bp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

app.register_blueprint(produtos_controller_bp)