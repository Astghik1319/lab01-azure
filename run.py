from flask import Flask
from flask import render_template
from flask import request
from flask import abort, send_from_directory
from flask import Flask, render_template, request
from AzureDB import AzureDB

import os
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP post user %s password %s' % (username, request.form['password'])
    else:
        return 'HTTP get for user %s' % username


@app.route('/error_denied')
def error_denied():
    abort(401)


if __name__ == '__main__':
    app.run(debug=True)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.route("/")
def index():
 msg = Message('Hello', sender = 'yourId@gmail.com', recipients = ['someone1@gmail.com'])
 msg.body = "Hello Flask message sent from Flask-Mail"
 mail.send(msg)
 return "Sent"
if __name__ == '__main__':
 app.run(debug = True)
 
 @app.route('/')
def hello():
 with AzureDB() as a:
 data = a.azureGetData()
 return render_template("result.html", data = data)
if __name__ == '__main__':
 app.run(debug=True)
