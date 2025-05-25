<template>
  <div class="form-wrapper">
    <h2>Вход</h2>
    <form @submit.prevent="login">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Пароль" />
      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const router = useRouter()

const login = async () => {
  try {
    const res = await axios.post('/auth/jwt/create/', {
      email: email.value,
      password: password.value
    })
    localStorage.setItem('access', res.data.access)
    localStorage.setItem('refresh', res.data.refresh)
    router.push('/')
  } catch (err) {
    alert('Ошибка входа')
  }
}
</script>

<style scoped>
.form-wrapper {
  max-width: 400px;
  margin: 0 auto;
}
</style>
