<script setup>

</script>
<template>
<div class="main-wrapper ">
  <div class="overlay">
<div class="container  ">
  <nav class="navbar navbar-expand-lg bg-body-tertiary p-3 rounded shadow-sm">
    <div class="container-fluid">
      <!-- Логотип и название -->
      <a class="navbar-brand d-flex align-items-center" href="/">
        <img src="https://avatars.mds.yandex.net/i?id=1327dc68e4571753af091806e155a1a1b5f93b63-5403234-images-thumbs&n=13" alt="Logo" width="80" height="80" class="d-inline-block align-text-top me-2">
        <span class="fs-5 fw-bold">Федерация дзюдо России</span>
      </a>


      <!-- Кнопки входа/регистрации -->
      <div class="d-flex">
        <a href="/login" class="btn btn-outline-primary me-2">Войти</a>
        <a href="/register" class="btn btn-primary">Регистрация</a>
      </div>
    </div>
  </nav>
    <div> <router-view /></div>
  </div>
  </div></div>
</template>
<style scoped>


.main-wrapper {
  background-image: url("https://e7.pngegg.com/pngimages/208/973/png-clipart-jujutsu-judo-karate-dan-kata-karate-white-hand.png");
  background-size: contain; /* вся картинка влезет */
  background-repeat:repeat-x;
  background-position: center;
  /*background-attachment: fixed;*/
  min-height: 100vh;
  position: relative;
}

.overlay {
  background-color: rgba(255, 255, 255, 0.75); /* белый полупрозрачный фон */
  min-height: 100vh;
  padding: 20px;
  background-attachment: fixed; /* <-- ключевой параметр */
}
</style>