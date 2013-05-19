from flask import Flask
app = Flask(__name__)

@app.route('/<int:quote_id>')
def quote_page(quote_id):
    return 'Hello James! %d' % quote_id

@app.route('/')
def main_page():
    return 'Main page'

if __name__ == '__main__':
    app.run(debug=True)