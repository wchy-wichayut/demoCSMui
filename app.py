from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask.helpers import make_response


app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('login.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
   return render_template('formContact.html')


@app.route('/status')
def status():
   return render_template('statusView.html')


@app.route('/post_data')
def post_data():
    post_data = request.get_json()
    print(post_data)


@app.route('/liff_contact')
def liff_contact():
   return render_template('/line_liff/lineLiffContact.html')


@app.route('/test_login')
def test_login():
   return render_template('/line_liff/loginTest.html')


@app.route('/sdata', methods=['GET', 'POST']) 
def sdata():
    if request.method == 'POST':
        sdata = request.get_json()
        print(sdata)
        return make_response(sdata)


if __name__ == '__main__':
    app.run(debug=True, port=5510)