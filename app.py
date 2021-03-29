from flask import Flask, render_template, redirect, url_for, flash
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = 'nesavjoh494+-*/'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessages(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

@app.route('/')
def chat():
    return redirect(url_for('example'))

@app.route('/chat')
def example():
    return render_template('chat.html')

if __name__ == '__main__':
    app.run(debug=True)