#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ
import urlparse
import psycopg2
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

urlparse.uses_netloc.append('postgres')
url = urlparse.urlparse(environ.get('DATABASE_URL'))

db_credentials = 'dbname=%s user=%s password=%s host=%s port=%s' % (
            url.path[1:], url.username, url.password, url.hostname, url.port)

def connect():
    return psycopg2.connect(db_credentials)

def get_quote(id=None):
    conn = connect()
    cur = conn.cursor()
    if id is None:
        cur.execute('''
            SELECT id, quote, author FROM quotes ORDER BY random() LIMIT 1;
                    ''')
    else:
        cur.execute('SELECT id, quote, author from quotes where id=%s LIMIT 1;',
                    (id,))
    quote = cur.fetchone()
    cur.close()
    conn.close()
    return {'id': quote[0], 'text': quote[1], 'author': quote[2]}