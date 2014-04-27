#!/usr/bin/env python
# -*- coding: utf-8 -*-


def link(url, text):
    return '<a href="{url}" > {text} </a>'.format(**locals())
