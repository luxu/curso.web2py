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
    Post.created_on.represent = lambda valor,row: prettydate(valor)
    Post.category.represent = lambda categories,row: ','.join(
        db.category[cat].name for cat in categories
    )
    Post.id.represent = lambda value,row: A(
        value,
        _class="btn btn-primary btn-mini",
        _href=URL('post',
                  'edit',
                  args=value)
    )
    grid = SQLFORM.grid(Post)
    return dict(grid=grid)

def exemplo_smartgrid():
    grid = SQLFORM.smartgrid(db.blog, linked_tables=['post'])
    return dict(grid=grid)


