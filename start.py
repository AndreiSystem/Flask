from flask import Flask, render_template, request, redirect
from files import ler_produto, salvar_produto

app = Flask(__name__)
nome = 'Hbsis'
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/listagem')
def listagem():
    return render_template('listagem.html', produtos=ler_produto())


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastro.html')


@app.route('/salvar')
def salvar():
    lista_cadastro = {}

    cerveja = request.args['cerveja']
    teor = request.args['teor']
    tipo = request.args['tipo']
    valor = float(request.args['valor'])

    lista_cadastro['cerveja'] = cerveja
    lista_cadastro['teor'] = teor
    lista_cadastro['tipo'] = tipo
    lista_cadastro['valor'] = valor

    salvar_produto(lista_cadastro)

    return redirect('/listagem')


app.run(debug=True)
