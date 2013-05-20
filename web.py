#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response, redirect
import db
import json

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
    #json = '{"text": "Knowledge is gained in many schools.", "author": "Hawaiian Proverb", "id": 17580}'
    return Response(json_data, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)