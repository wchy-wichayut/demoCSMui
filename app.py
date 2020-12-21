from flask import Flask, render_template, jsonify, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():

    return render_template('login.html')


@app.route('/contact', methods=["GET", "POST"])
def contact():
   return render_template('formContact.html')


@app.route('/post_data')
def post_data():
    post_data = request.get_json()
    print(post_data)


if __name__ == '__main__':
    app.run(debug=True, port=5510)