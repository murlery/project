<script setup>

</script>
<template>
  <div class="container">
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">
          <img
            src="https://images.squarespace-cdn.com/content/v1/5aecd1beb27e39b2997a8bf4/1525727401682-QRVGLHTEWQDBMKT7V401/Tattoo1+Logo-Black_white.png"
            alt="Логотип" height="30" class="me-2">
        </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
          aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-between" id="navbarNavAltMarkup">
          <div class="navbar-nav">
            <router-link class="nav-link active" aria-current="page" to="/">Татуировки</router-link>
            <router-link class="nav-link" to="/styles">Стили татуировок</router-link>
            <router-link class="nav-link" to="/prices">Цены</router-link>
            <router-link class="nav-link" to="/tattooArtists">Тату мастера</router-link>
            <router-link class="nav-link" to="/tatooStudios">Тату студии</router-link>
          </div>
          <ul class="navbar-nav">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown"
                aria-expanded="false">
                Пользователь
              </a>
              <ul class="dropdown-menu">
                <li>
                  <a class="dropdown-item" href="/admin">
                    админка
                  </a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>



    <div> <router-view /></div>
  </div>
</template>
<style scoped></style>