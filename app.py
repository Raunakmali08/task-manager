from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Configure SQLite Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'tasks.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Task Model definition
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(20), default='pending') # pending or done

    def to_dict(self):
        """Serialize Task object to dictionary"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status
        }

# Create database tables before first request
with app.app_context():
    db.create_all()

# ==========================================
# Frontend Route
# ==========================================

@app.route('/')
def index():
    """Serve the main frontend HTML application."""
    return render_template('index.html')

# ==========================================
# REST API Endpoints for Full CRUD
# ==========================================

# READ: Get all tasks
@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.order_by(Task.id.desc()).all()
    return jsonify([task.to_dict() for task in tasks])

# CREATE: Add a new task
@app.route('/api/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400
    
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'pending')
    )
    db.session.add(new_task)
    db.session.commit()
    
    return jsonify(new_task.to_dict()), 201

# UPDATE: Modify an existing task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
        
    data = request.get_json()
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.status = data.get('status', task.status)
    
    db.session.commit()
    
    return jsonify(task.to_dict())

# DELETE: Remove a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
        
    db.session.delete(task)
    db.session.commit()
    
    return jsonify({'message': 'Task deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
