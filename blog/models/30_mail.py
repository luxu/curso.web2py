# mail
mail = auth.settings.mailer
mail.settings.server = "logging" or "smtp.gmail.com:587"
mail.settings.sender = "admin@site.com"
mail.settings.login = "user:password"

# signals


def notifica(form):
    user = form.vars
    mail.send(
        to=mail.settings.sender,
        subject="Usuário %(first_name)s pendente" % user,
        message="<html>Você tem um novo usuário para aprovar "
        "%(first_name)s - %(email)s </html>" % user
    )

auth.settings.register_onaccept = notifica
