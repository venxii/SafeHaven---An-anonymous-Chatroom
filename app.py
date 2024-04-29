from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__,static_url_path='/static')
socketio = SocketIO(app, cors_allowed_origins="*")

 
@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)
    # send() function will emit a message vent by default

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/chat")
def message():
    return render_template("userpage.html")


if __name__ == "__main__":
    app.run(debug=True)
