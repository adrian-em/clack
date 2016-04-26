from flask import Flask, render_template, request, session
import cgi
import datetime
import time
import json


app = Flask(__name__)


app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'Q\xbb\x0f\xae\xedO\xf0:\tv\xfaMKgX4\x95\xdfo\x18\xc7lIM'
app.config['PUSHER_CHAT_APP_ID'] = '201352'
app.config['PUSHER_CHAT_APP_KEY'] = '5d0ca78191576915a474'
app.config['PUSHER_CHAT_APP_SECRET'] = '856bd602368c0aea58d1'

import pusher

pusher_client = pusher.Pusher(
    app_id=app.config['PUSHER_CHAT_APP_ID'],
    key=app.config['PUSHER_CHAT_APP_KEY'],
    secret=app.config['PUSHER_CHAT_APP_SECRET'],
    ssl=True
)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/setname/', methods=['POST'])
def set_name():
    session['name'] = request.form['name']

    return "Succesful"


@app.route('/pusher/auth/', methods=['POST'])
def pusher_authentication():
    auth = pusher_client.authenticate(
        channel=request.form['channel_name'],
        socket_id=request.form['socket_id'],
        custom_data={
            'user_id': session['name']
        }
    )

    return json.dumps(auth)


@app.route('/messages/', methods=['POST'])
def new_message():
    name = request.form['name']
    text = cgi.escape(request.form['text'])
    channel = request.form['channel']

    now = datetime.datetime.now()
    timestamp = time.mktime(now.timetuple()) * 1000
    pusher_client.trigger("presence-" + channel, 'new_message', {
        'text': text,
        'name': name,
        'time': timestamp
    })

    return "Sucessful"


if __name__ == "__main__":
    app.run()