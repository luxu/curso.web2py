from gluon.storage import Storage

config = Storage(
    db=Storage(),
    auth=Storage(),
    mail=Storage()
)

if request.is_local:
    config.db.uri = 'sqlite://blog_dev.sqlite'
    config.db.check_reserved = ['all']  # somente desenvolvimento
else:
    config.db.uri = 'sqlite://blog_prod.sqlite'
    config.db.migrate_enabled = False

config.db.pool_size = 10


# objetos
db = DAL(**config.db)  # socket existente no pool ou cria novo socket
