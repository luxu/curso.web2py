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

Anotações da aula 4:
Exemplo de logging está na raiz e como utilizar é só ler o arquivo.
No model está a instância do logger.

Nome Handler - Saída
consoleHandler - console
rotatingFileHandler - arquivo
messageBoxHandler - sysnotify

http://127.0.0.1:8000/user/<item>
login - autenticar
register - cadastrar
retrieve_password - esqueci a senha
profile - perfil do usuário editável
logout - saída do sitema


auth é callable que retorna formulário de autenticação

auth.user ou session.auth.user para informações do usuário autenticado
auth.user_id e auth.user_groups também estão disponíveis

response.download(request, db) - media não fica no banco de dados
mas seu caminho sim

Para adicionar campos extras ao usuário
auth.settings.extra_fields['auth_user'] = [lista de campos extras]
Exemplo de desabilitar registro
auth.settings.actions_disabled = ['register']

'''


def home():
    return "Welcome to my blog"


def contact():
    return "form"


def about():
    return "sobre o autor"


def user():
    logger.info(request.args)
    if request.args(0) == 'register':
        fields = ['bio', 'photo', 'gender']
        for field in fields:
            db.auth_user[field].readable = False
            db.auth_user[field].writable = False
    return auth()


def register():
    return auth.register()


def login():
    return auth.login()


def account():
    '''Cuidado pois suário já autenticado irá sofrer redirecionamento'''
    return{
        'login': auth.login(),
        'register': auth.register()
    }


def download():
    return response.download(request, db)
