from flask import Flask, render_template, url_for
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

 
@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)
    # send() function will emit a message vent by default

@app.route("/")
def index():
    # Generate URL for the 'message' route
    chat_url = url_for('message')
    return render_template("index.html", chat_url=chat_url)


@app.route("/chat")
def message():
    return render_template("userpage.html")


if __name__ == "__main__":
    app.run(debug=True)
