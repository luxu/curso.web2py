#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Anotações da aula 1:

Toda função que apresenta parâmetros não é exposta:
Ex:
    def soma(x, y):
        return x + y

Existe no objeto request variáveis vars, post_vars e get_vars separadas.

Utilize redirect('http://www.google.com') para redirecionar para outra página

Retorno deve ser serializável(pode ser convertido para string).

Para renderizar uma página:
return response.render("blah.html", {"nome": "Bruno"})

Anotações aula 2:
SQLFORM recebe Table ou Query

check_reserved pode ser utilizado somente com um banco específico
ex: check_reserved = ['mysql']
deve ser utilizado somente em desenvolvimento

default do field pode ser função que retorna um valor

Anotações da aula 3:

query = db.blog.id == 1  # virará objeto query
query2 = db.blog.title.startswith('meu') # like meu%
query & query2 # retorna query AND query2
query | query2 # retorna query OR query2
query &= query2 # realiza and e guarda retorno em query

db(queryset).operation()
db(queryset)._operation() # verifica sql gerada

db(queryset).operation() retorna lista de rows
rows tem metodo json e xml do resultado, assim como exporta csv
row = rows[0]
cada row representa tupla retornada e caso seja alterada sua mudança
será refletida no banco de dados.

'''


def home():
    return "Welcome to my blog"


def contact():
    return "form"


def about():
    return "sobre o autor"


def user():
    return "user"


def download():
    "download"
