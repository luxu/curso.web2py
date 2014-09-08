@auth.requires_membership('admin')
def category():
    form = SQLFORM(
        Category,
        submit_button='enviar'
    )
    if form.process().accepted:
        response.flash = 'categoria adicionada adicionado'
    elif form.errors:
        response.flash = 'formulário possui erro'
    response.view = 'manager/default.html'
    return {'form': form}


@auth.requires_membership('admin')
def blogs():
    form = SQLFORM(
        Blog,
        submit_button='enviar'
    )
    if form.process().accepted:
        response.flash = 'blog adicionado'
    elif form.errors:
        response.flash = 'formulário possui erro'
    response.view = 'manager/default.html'
    return {'form': form}


@auth.requires_login()
def users():
    pass
