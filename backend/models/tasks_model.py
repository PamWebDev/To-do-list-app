""" 
Este módulo define el módelo de tabla para las tareas (tasks)
"""

import enum
from sqlalchemy import Column, Integer, String, Text, Enum, DateTime
from sqlalchemy.sql import func
from database.db import db

class TaskStatus(enum.Enum):
    PENDING = 'Pendiente'
    IN_PROGRESS = 'En proceso'
    COMPLETED = 'Completada'

class Tasks(db.Model):
    """ Modelo de tabla para las tareas """
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(TaskStatus), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    def to_dict(self):
        """
        Función para convertir los registros de la tabla en diccionarios
        """
        return {
            'id': self.id,
            'title': self.title,
            'decription': self.description,
            'status': self.status.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __str__(self):
        return f'Task ID: {self.id}'