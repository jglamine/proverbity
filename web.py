#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response, redirect
import db
import json
from os import environ

app = Flask(__name__)

@app.route('/')
@app.route('/<int:quote_id>')
def quote_page(quote_id=None):
    if quote_id is None:
        return redirect(str(db.get_quote()['id']))
    else:
        quote = db.get_quote(quote_id)
        return render_template('quote_page.html', quote_text=quote['text'],
                               quote_author=quote['author'])

@app.route('/ajax/random_quote.json')
def ajax_quote():
    json_data = json.dumps(db.get_quote())
    return Response(json_data, mimetype='application/json')


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)