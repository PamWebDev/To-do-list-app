# To-Do List Application

## Descripción

Este es un proyecto de **lista de tareas** (To-Do List) que permite gestionar tareas mediante una aplicación web. El frontend está desarrollado con **Vue.js** y el backend con **Flask y Python**. La aplicación actualmente permite visualizar las tareas, con el objetivo a futuro de que se puedan crear, editar y eliminar tareas dentro de la misma aplicación. Las tareas son almacenadas en una base de datos **PostgreSQL**.

## Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Frontend**: Vue.js
- **Base de datos**: PostgreSQL
- **Entorno de desarrollo**: Node.js (para el frontend)

---

## Configuración y Ejecución de la Aplicación

### 1. **Clonar el repositorio**

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu_usuario/To-do-list-app.git
cd to-do-list-app 
```

### 2. **Configurar el Backend**
**a. Instalar dependencias**

Dentro del directorio del backend, instala las dependencias necesarias con pip:

```bash
cd backend
pip install -r requirements.txt
```

**b. Configurar la base de datos**

Asegúrate de tener PostgreSQL configurado en tu máquina. Crea una base de datos para el proyecto y configura la conexión en tu archivo de configuración.

El archivo .env (o cualquier archivo de configuración que estés utilizando) debe contener las credenciales para la base de datos, por ejemplo:

```bash
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/nombre_de_la_base_de_datos
```

**c. Ejecutar el backend**

Inicia el servidor de desarrollo de Flask con el siguiente comando:

```bash
flask run
```

El servidor backend estará disponible en http://localhost:5000.

### 3. **Configurar el Frontend**
**a. Instalar dependencias**

Dentro del directorio del frontend, instala las dependencias necesarias con npm:

```bash
cd frontend
npm install
```

**b. Ejecutar el frontend**

Inicia el servidor de desarrollo de Vue.js con el siguiente comando:

```bash
npm run dev
```

El frontend estará disponible en http://localhost:3000.

## Funcionalidades Actuales de la Aplicación
- Visualización de tareas: Muestra todas las tareas almacenadas en la base de datos.
### Futuras Funcionalidades:
- Crear tarea: Permite agregar nuevas tareas con título, descripción y estado.
- Editar tarea: Permite modificar el título, descripción o estado de una tarea existente.
- Eliminar tarea: Permite eliminar tareas de la lista.

## Decisiones Técnicas
A continuación, se describen algunas de las decisiones técnicas tomadas durante el desarrollo:

1. Backend con Flask: Se eligió Flask porque es un framework ligero y flexible que facilita la creación de APIs RESTful, lo que lo convierte en una excelente opción para este tipo de aplicaciones.

2. Frontend con Vue.js: Se optó por Vue.js debido a su facilidad de integración con otras tecnologías, su reactividad, y la posibilidad de estructurar componentes de manera modular y eficiente.

3. Base de datos PostgreSQL: Se utilizó PostgreSQL debido a su robustez, capacidad de manejar grandes volúmenes de datos, y su integración sencilla con SQLAlchemy en Flask.

4. Rutas de la API RESTful: Las rutas implementadas permiten crear, leer, actualizar y eliminar tareas a través de métodos HTTP estándar (GET, POST, PUT, DELETE), lo que sigue las mejores prácticas de desarrollo de APIs.

## Proceso de Aprendizaje
Durante el desarrollo de esta aplicación, aprendí nuevas tecnologías y enfoques. A continuación se describe cómo abordé el proceso de aprendizaje:

### Recursos utilizados
- **Documentación oficial de Flask:** La documentación oficial de Flask fue una fuente clave para entender cómo trabajar con rutas, solicitudes y conexión a bases de datos.

- **Documentación oficial de Vue.js:** Utilicé la documentación oficial de Vue.js para aprender sobre el sistema de componentes y la reactividad.

- **Tutoriales en línea:** Consulté tutoriales en freeCodeCamp para mejorar mis conocimientos en Vue.js y Flask.

- **IA:** Para consultas puntuales y verificación de los avances.

## Desafíos enfrentados y cómo los superé
1. **Manejo de errores en las solicitudes:** Al trabajar con las rutas de la API, tuve que aprender a manejar errores en las solicitudes (por ejemplo, cuando se intenta actualizar o eliminar una tarea que no existe). Esto lo resolví utilizando los métodos de Flask para capturar y devolver errores de manera adecuada.

2. **Comunicación entre el frontend y el backend:** Inicialmente, tuve problemas para comunicar el frontend (Vue.js) con el backend (Flask) debido a problemas de CORS. Esto se resolvió fácilmente utilizando el paquete flask-cors en el backend.

