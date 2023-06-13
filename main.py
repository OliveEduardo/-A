from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/calculadora')
def homepage():
    boas_vindas = ('Bem vindo!! Exemplo de Operação:http://localhost:5000/calculadora/sum/3/2 =5 ')
    return (boas_vindas)


@app.get('/calculadora/sum/<int:n1>/<int:n2>')
def soma(n1, n2):
    soma = n1 + n2
    return (soma)


@app.get('/calculadora/sub/<int:n1>/<int:n2>')
def subtracao(n1, n2):
    sub = n1 - n2
    return (sub)


@app.get('/calculadora/div/<int:n1>/<int:n2>')
def divisao(n1, n2):
    divisao = n1 / n2
    return (divisao)


@app.get('/calculadora/mult/<int:n1>/<int:n2>')
def multiplicar(n1, n2):
    mult = n1 * n2
    return (mult)
