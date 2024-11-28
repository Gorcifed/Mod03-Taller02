from flask import Flask, render_template
from controllers.controller_animal import animales_blueprint
import os

app = Flask(__name__, template_folder = "views")
app.register_blueprint(animales_blueprint)

@app.route('/')
def index():
    return render_template("Index.html")


if __name__ == '__main__':
    app.run(debug=True)