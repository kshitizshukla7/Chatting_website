from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'  # Secret key for session management
socketio = SocketIO(app)  # Initialize SocketIO for real-time communication

# Route to serve the chat page
@app.route('/')
def index():
    return render_template('index.html')

# Handle messages sent by clients
@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)  # Broadcast the message to all connected clients

if __name__ == '__main__':
    # Run the Flask-SocketIO server
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
