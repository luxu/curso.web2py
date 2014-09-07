def show():
    return "post"


def edit():
    return "edit post"


def delete():
    return "delete"

@auth.requires_login()
def add():
    logger.info(auth.user_id)
    logger.info(auth.user_groups)
    # logger.debug("Executando a funcao add")
    # logger.info(str(request.vars))
    # try:
    #     1/0
    # except ZeroDivisionError as erro:
    #     logger.error(str(erro))
    # return "add"
    return SQLFORM(Post).process()
