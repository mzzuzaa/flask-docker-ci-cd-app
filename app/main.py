
from flask import Flask, request, jsonify
import redis
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Redis setup
redis_client = redis.Redis(host='redis', port=6379)

# PostgreSQL setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    redis_client.incr('hits')
    count = redis_client.get('hits').decode('utf-8')
    return f"Hello! Page viewed {count} times."

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = Task(content=data['content'])
    db.session.add(task)
    db.session.commit()
    return jsonify({'message': 'Task added'}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': t.id, 'content': t.content} for t in tasks])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
