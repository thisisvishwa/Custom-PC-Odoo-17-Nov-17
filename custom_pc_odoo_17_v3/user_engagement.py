```python
import os
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from sklearn.externals import joblib

app = Flask(__name__)
socketio = SocketIO(app)

# Load AI model for product recommendation
ai_model = joblib.load('ai_model.pkl')

@app.route('/api/recommend', methods=['POST'])
def recommend_products():
    user_data = request.json
    recommended_products = ai_model.predict(user_data)
    return jsonify(recommended_products)

@socketio.on('connect')
def handle_connect():
    print('User connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('User disconnected')

@socketio.on('chat message')
def handle_chat_message(message):
    print('Received message: ', message)
    emit('chat message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))
```