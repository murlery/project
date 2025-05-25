<template>
  <div class="form-wrapper">
    <h2>Регистрация</h2>
    <form @submit.prevent="register">
      <input v-model="email" placeholder="Email" />
      <input v-model="password" type="password" placeholder="Пароль" />
      <select v-model="role">
        <option disabled value="">Выберите роль</option>
        <option value="athlete">Спортсмен</option>
        <option value="coach">Тренер</option>
      </select>
      <button type="submit" :disabled="!role">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const email = ref('')
const password = ref('')
const role = ref('')
const router = useRouter()

const register = async () => {
  if (!role.value) {
    alert('Пожалуйста, выберите роль')
    return
  }

  try {
    await axios.post('/auth/users/', {
      email: email.value,
      password: password.value,
      role: role.value
    })
    alert('Регистрация успешна!')
    router.push('/login')
  } catch (err) {
    alert('Ошибка регистрации')
  }
}
</script>

<style scoped>
.form-wrapper {
  max-width: 400px;
  margin: 0 auto;
}
select {
  margin: 10px 0;
  padding: 6px;
  width: 100%;
}
</style>
