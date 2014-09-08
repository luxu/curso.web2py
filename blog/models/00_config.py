from gluon.storage import Storage

config = Storage(
    db=Storage(),
    auth=Storage(),
    mail=Storage()
)

if request.is_local:
    config.db.uri = 'sqlite://blog_dev.sqlite'
    config.db.check_reserved = ['all']  # somente desenvolvimento
    response.generic_patterns = ['*']
else:
    config.db.uri = 'sqlite://blog_prod.sqlite'
    config.db.migrate_enabled = False

config.db.pool_size = 10


# objetos
db = DAL(**config.db)  # socket existente no pool ou cria novo socket

# logging
import logging
logger = logging.getLogger("web2py.app.blog")
logger.setLevel(logging.DEBUG)  # INFO, DEBUG, WARNING, ERROR, CRITICAL

# auth
from gluon.tools import Auth
auth = Auth(db, controller="initial", function="user")

# auth settings
auth.settings.remember_me_form = False
auth.settings.formstyle = 'divs'
auth.settings.login_next = URL('initial', 'home')
auth.settings.registration_requires_verification = True
#auth.settings.registration_requires_approval = True


# auth messages
auth.messages.login_button = 'Entre'

# auth fields
auth.settings.extra_fields['auth_user'] = [
    Field('bio', 'text'),
    Field('photo', 'upload'),
    Field('gender', requires=IS_IN_SET(["male", "female"]))
]
auth.define_tables()

response.title = 'blog'
response.meta.keywords = "chave,outra e outra"
