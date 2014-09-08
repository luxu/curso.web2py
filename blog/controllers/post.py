from customvalidators import valida


def show():
    return "post"


def edit():
    return "edit post"


def delete():
    return "delete"


@auth.requires(auth.has_membership('admin') or auth.has_membership('editor'))
def add():
    form = SQLFORM(
        Post,
        submit_button='enviar'
    )
    if form.process(onvalidation=valida).accepted:
        response.flash = 'post adicionado'
    elif form.errors:
        response.flash = 'formulário possui erro'
    response.view = 'manager/default.html'
    return {'form': form}
    # logger.info(auth.user_id)
    # logger.info(auth.user_groups)
    # logger.debug("Executando a funcao add")
    # logger.info(str(request.vars))
    # try:
    # 1/0
    # except ZeroDivisionError as erro:
    # logger.error(str(erro))
    # return "add"
    # return SQLFORM(Post).process()
