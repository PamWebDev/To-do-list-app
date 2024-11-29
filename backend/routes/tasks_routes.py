"""
Este modulo contiene la ruta a /tasks y sus configuraciones
"""
from flask import Blueprint
from flask import jsonify, request
from database.db import db
from models.tasks_model import Tasks
from datetime import datetime, timezone

tasks_routes = Blueprint('tasks_routes', __name__)

@tasks_routes.route('/api/tasks', methods=['GET'])
def get_tasks():
    """
    Obtiene la lista completa de las tareas
    """
    return jsonify([task.to_dict() for task in Tasks.query.all()])

@tasks_routes.route('/api/tasks', methods=['POST'])
def create_task():
    """
    Crea una tarea nueva
    """
    data = request.get_json()
    task = Tasks(
        title = data['title'],
        description=data['description'],
        status=data['status'],
        created_at=data.get('createdAt', datetime.now(timezone.utc)),
        updated_at=data.get('updatedAt', datetime.now(timezone.utc))
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201

@tasks_routes.route('/api/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    data = request.get_json()
    task = Tasks.query.get_or_404(id)
    task.title = data['title']
    task.description = data['description']
    task.status = data['status']
    task.updated_at = data.get('updatedAt', datetime.now(timezone.utc))
    db.session.commit()
    return jsonify(task.to_dict())

@tasks_routes.route('/api/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Tasks.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return '', 204

