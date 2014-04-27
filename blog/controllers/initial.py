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
