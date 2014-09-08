from customvalidators import IS_NOT_BAZINGA
Post.blog.requires = IS_IN_DB(db, 'blog.id', '%(title)s')
Post.title.requires = [
    IS_NOT_EMPTY(),
    IS_NOT_BAZINGA(),
    IS_NOT_IN_DB(db, 'post.title')
]
Post.slug.compute = lambda registro:IS_SLUG()(registro.title)[0]
Post.category.widget = SQLFORM.widgets.checkboxes.widget
Post.category.requires = IS_IN_DB(db, 'category.id', '%(name)s', multiple=True)
