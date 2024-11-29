"""
Este modulo contiene la ruta a /tasks y sus configuraciones
"""
from flask import Blueprint
from flask import jsonify
from database.db import db
from models.tasks_model import Tasks

tasks_routes = Blueprint('tasks_routes', __name__)

@tasks_routes.route('/api/tasks', methods=['GET'])
def get_tasks():
    """
    Obtiene la lista completa de las tareas
    """
    return jsonify([task.to_dict() for task in Tasks.query.all()])
