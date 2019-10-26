from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/hit_me')
def hit_me():
    arguments = request.args.to_dict()
    return render_template('hit_me.html', firstName=arguments['firstName'], lastName=arguments['lastName'])


@app.route('/')
def index():
    return 'Deployed Flask project on Heroku by ~aady95'


app.run('127.0.0.1',port=5000, debug=True)