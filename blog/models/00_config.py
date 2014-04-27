from gluon.storage import Storage

config = Storage(
    db=Storage(),
    auth=Storage(),
    mail=Storage()
)

if request.is_local:
    config.db.uri = 'sqlite://blog_dev.sqlite'
else:
    config.db.uri = 'sqlite://blog_prod.sqlite'
config.db.pool_size = 10
