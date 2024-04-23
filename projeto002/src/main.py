from flask import Flask, request
from defs import selection_sort, bubble_sort, quick_sort, merge_sort, insertion_sort

app = Flask(__name__)

@app.route("/insertion")
def insertion():
    try:
        cidades = insertion_sort()
        return cidades
    except Exception as e:
        return f"Erro na rota: {e}"

@app.route('/selection')
def selection():
    try:
        cidades = selection_sort()
        return cidades
    except Exception as e:
        return f"Erro na rota: {e}"

@app.route('/bubble')
def bubble():
    try:
        cidades = bubble_sort()
        return cidades
    except Exception as e:
        return f"Erro na rota: {e}" 

@app.route('/quick')
def quick():
    try:
        cidades = quick_sort()
        return cidades
    except Exception as e:
        return f"Erro na rota: {e}"
    
@app.route('/merge')
def merge():
    try:
        cidades = merge_sort()
        return cidades
    except Exception as e:
        return f"Erro na rota: {e}"
app.run(debug=True)