<template>
  <div>
    <h1>Admin Dashboard</h1>
    <p>Users: {{ metrics.users }}</p>
    <p>Subscriptions: {{ metrics.subscriptions }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const metrics = ref({})

onMounted(async () => {
  const res = await fetch('/api/v1/admin/metrics', {
    headers: { Authorization: `Bearer ${localStorage.token}` }
  })
  metrics.value = await res.json()
})
</script>
