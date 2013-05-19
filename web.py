from flask import Flask, render_template, Response, redirect

app = Flask(__name__)

@app.route('/')
@app.route('/<int:quote_id>')
def quote_page(quote_id=None):
    if quote_id is None:
        return redirect('/0001')
    else:
        return render_template('quote_page.html', quote_text='this quote',
                               quote_author='John')

@app.route('/ajax/random_quote.json')
def ajax_quote():
    json = '{"text": "Knowledge is gained in many schools.", "author": "Hawaiian Proverb", "id": 17580}'
    return Response(json, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)