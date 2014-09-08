#!/usr/bin/env python
# -*- coding: utf-8 -*-


class IS_NOT_BAZINGA(object):

    def __init__(self, error_message="ńão pode ter bazinga!"):
        self.error_message = error_message

    def __call__(self, value):
        if 'bazinga' in value.lower():
            return (value, self.error_message)
        else:
            return (value, None)

def valida(form):
    if not "bazinga" in form.vars.post_body:
        form.errors.post_body = "O post tem de ter a palavra bazinga"
