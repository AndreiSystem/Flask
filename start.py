from flask import Flask, render_template

app = Flask(__name__)
nome = 'Hbsis'
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/listagem')
def listagem():
    return render_template('listagem.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')

@app.route('/salvar')
def salvar():
    return 'salvando'

app.run(debug = True)