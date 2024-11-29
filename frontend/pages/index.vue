<template>
    <div>
      <h1>Lista de Tareas</h1>
      <ul>
        <li v-for="task in tasks" :key="task.id">
          <p>{{ task.title }}</p>
          <p>{{ task.description }}</p>
          <p>{{ task.status }}</p>
          <p>{{ task.createdAt }}</p>
          <button @click="deleteTask(task.id)">Eliminar</button>
          <button @click="editTask(task.id)">Editar</button>
        </li>
      </ul>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const tasks = ref([])

const fetchTasks = async() => {
    const res = await fetch('http://localhost:5000/api/tasks')
    tasks.value = await res.json()
}

const deleteTask = async(id) => {
    await fetch(`/api/tasks/${id}`, { method: 'DELETE'})
    fetchTasks()
}

const editTask = (id) => {

}

onMounted(() => {
    fetchTasks()
})
</script>
