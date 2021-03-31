from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask.helpers import make_response


app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('login.html')

@app.route('/regis', methods=["GET", "POST"])
def regis():
   return render_template('register.html')

@app.route('/project')
def project():
   return render_template('projectUser.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
   return render_template('formContact.html')


@app.route('/status')
def status():
   return render_template('statusView.html')

@app.route('/rating')
def rating():
   return render_template('evaluateWork.html')




if __name__ == '__main__':
    app.run(debug=True, port=5510)