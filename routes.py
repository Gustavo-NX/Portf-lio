from portifolio import app
from flask import render_template , url_for
import emoji

# fazendo rotas
@app.route("/")
def homepage():
    titulo = "NIGHTX"
    return render_template('homepage.html' , titulo=titulo)

@app.route('/informacoes')
def info():
    return render_template('informacoes.html')