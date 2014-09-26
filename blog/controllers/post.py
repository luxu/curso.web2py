from customvalidators import valida


def show():
    return "post"


@auth.requires(auth.has_membership('admin') or auth.has_membership('editor'))
def edit():
    post_id = request.args(0)
    if not Post[post_id]:
        redirect(URL('posts'))
    response.view = 'manager/default.html'
    return dict(form=SQLFORM(Post, post_id) .process())


def delete():
    return "delete"


@auth.requires(auth.has_membership('admin') or auth.has_membership('editor'))
def add():
    Post.post_body.widget = ckeditor.widget
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


@auth.requires(auth.has_membership('admin') or auth.has_membership('editor'))
def posts():
    Post.created_on.represent = lambda valor: prettydate(valor)
    Post.category.represent = lambda categories: ','.join(
        db.category[cat].name for cat in categories
    )
    Post.id.represent = lambda value: A(
        value,
        _class="btn btn-primary btn-mini",
        _href=URL('post',
                  'edit',
                  args=value)
    )
    rows = db(db.post).select(orderby=~db.post.created_on)
    columns = ['id', 'title', 'post_body', 'created_on', 'category']
    table = TABLE(_class="table table-striped")
    table.append(TR(*[B(col.replace('_', ' ').capitalize())
                      for col in columns]))
    for row in rows:
        tr = TR()
        for col in columns:
            if Post[col].represent:
                tr.append(Post[col].represent(row[col]))
            else:
                tr.append(TD(row[col]))
    table.append(tr)
    return dict(postagens=table)


def exemplo_factory():
    form = SQLFORM.factory(
        Field("email", requires=IS_EMAIL()),
        Field("receber_news", "boolean")
    )
    if form.process().accepted:
        response.flash = 'OK'
    return dict(form=form)


def add2():
    form = SQLFORM(
        Post,
        submit_button='enviar'
    )
    if form.process(onvalidation=valida).accepted:
        response.flash = 'post adicionado'
    elif form.errors:
        response.flash = 'formulário possui erro'
    return {'form': form}
