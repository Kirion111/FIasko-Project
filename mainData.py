from flask import Flask

#Main

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Pagina principal</p>"