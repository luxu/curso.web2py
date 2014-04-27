#!/usr/bin/env python
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from framework import link


def application(env, start_response):
    python_link = link('http://python.org', 'PYTHON')
    response_body = '''<h1>Hello World</h1>
    <br/>
    {link}'''.format(link=python_link)
    content_length = len(response_body)
    status = "200 OK"
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(content_length)),
    ]
    start_response(status, response_headers)
    return [response_body]

http = make_server('localhost', 8051, application)
print("Servindo em http://localhost:8051")
http.serve_forever()
