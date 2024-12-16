<script setup>
import axios from "axios";
import { computed, onBeforeMount, ref } from "vue";
import _ from "lodash";
import Cookies from "js-cookie";

const tattoos = ref([]);
const styles = ref([]);
const prices = ref([]);
const tattooArtists = ref([]);
const tattoosPictureRef = ref();
const tattooAddImageUrl = ref();
const tattooEditPictureRef = ref(); // Используйте только для редактирования
const tattooEditImageUrl = ref();
const selectedImage = ref('');


const tattooToAdd = ref({});
const tattooToEdit = ref({});


async function onTattoosAdd() {
  const formData = new FormData();
  formData.append('picture', tattoosPictureRef.value.files[0]);
  formData.set('name', tattooToAdd.value.name);
  formData.set('style', tattooToAdd.value.style);
  formData.set('price', tattooToAdd.value.price);
  formData.set('tattooArtist', tattooToAdd.value.tattooArtist);

  await axios.post("/api/tattoos/", formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
  await fetchTattoos(); // переподтягиваю
}

async function fetchTattooArtist() {
  const r = await axios.get("/api/tattooArtists/");
  console.log(r.data);
  tattooArtists.value = r.data;
}

async function fetchPrices() {
  const r = await axios.get("/api/prices/");
  console.log(r.data);
  prices.value = r.data;
}

async function fetchStyles() {
  const r = await axios.get("/api/styles/");
  console.log(r.data);
  styles.value = r.data;
}

async function fetchTattoos() {
  const r = await axios.get("/api/tattoos/");
  console.log(r.data);
  tattoos.value = r.data;
}

async function onTattooRemoveClick(tattoo) {
  await axios.delete(`/api/tattoos/${tattoo.id}/`);
  await fetchTattoos(); // переподтягиваю
}

async function onTattooEditClick(tattoo) {
  tattooToEdit.value = { ...tattoo, tattooStyle: tattoo.tattooStyle.id };
  tattooEditImageUrl.value = tattoo.picture;
}

async function onTattooUpdate() {
  const formData = new FormData();

  // Добавляем изображение, если оно было загружено для редактирования
  if (tattooToEdit.value.picture) {
    formData.append('picture', tattooToEdit.value.picture);
  }

  formData.set('name', tattooToEdit.value.name);
  formData.set('style', tattooToEdit.value.style);
  formData.set('price', tattooToEdit.value.price);
  formData.set('tattooArtist', tattooToEdit.value.tattooArtist);

  await axios.put(`/api/tattoos/${tattooToEdit.value.id}/`, formData, {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  });
  await fetchTattoos(); // переподтягиваю
}

async function tattoosEditPictureChange(event) {
  const file = event.target.files[0];
  if (file) {
    tattooEditImageUrl.value = URL.createObjectURL(file);
    tattooToEdit.value.picture = file; // Сохраняем файл в tattooToEdit
  }
}

async function tattoosAddPictureChange() {
  tattooAddImageUrl.value = URL.createObjectURL(tattoosPictureRef.value.files[0]);
}

async function showImageModal(imageUrl) {
  selectedImage.value = imageUrl;
}

onBeforeMount(async () => {
  axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
  await fetchTattoos();
  await fetchStyles();
  await fetchPrices();
  await fetchTattooArtist();
});
</script>

<template>
  <div class="container-fluid">
    <!-- Modal -->
    <div class="modal fade" id="editModal" tabindex="-1" aria-labelledby="editModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="editModalLabel">Редактирование</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col">
                <div class="form-floating">
                  <input type="text" class="form-control" v-model="tattooToEdit.name" required />
                  <label for="floatingInput">Название татуировки</label>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-auto">
                <input class="form-control" type="file" ref="tattooEditPictureRef" @change="tattoosEditPictureChange">
              </div>
            </div>
            <div class="row">
              <div class="col-auto">
                <div class="form-floating">
                  <select class="form-select" v-model="tattooToEdit.style" required>
                    <option value="" disabled>Выберите стиль</option>
                    <option :value="s.id" v-for="s in styles" :key="s.id">
                      {{ s.name }}
                    </option>
                  </select>
                  <label for="floatingInput">Стиль татуировки</label>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-auto">
                <div class="form-floating">
                  <select class="form-select" v-model="tattooToEdit.price" required>
                    <option value="" disabled>Выберите цену</option>
                    <option :value="p.id" v-for="p in prices" :key="p.id">
                      {{ p.name }}
                    </option>
                  </select>
                  <label for="floatingInput">Цена татуировки</label>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-auto">
                <div class="form-floating">
                  <select class="form-select" v-model="tattooToEdit.tattooArtist" required>
                    <option value="" disabled>Выберите тату мастера</option>
                    <option :value="a.id" v-for="a in tattooArtists" :key="a.id">
                      {{ a.name }}
                    </option>
                  </select>
                  <label for="floatingInput">Тату мастер</label>
                </div>
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
              Закрыть
            </button>
            <button type="button" class="btn btn-dark" data-bs-dismiss="modal" @click="onTattooUpdate">
              Сохранить изменения
            </button>
          </div>
        </div>
      </div>
    </div>




    <!-- Modal -->
    <div class="modal fade" id="imgModal" tabindex="-1" aria-labelledby="imgModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="imgModalLabel">Татуировка</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <div class="row">
              <div class="col">

                <img :src="selectedImage" alt="tattoo" style="max-width: 100%; height: auto;">
              </div>
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-dark" data-bs-dismiss="modal">
              Закрыть
            </button>

          </div>
        </div>
      </div>
    </div>

    <div>
      <div class="p-2">
        <form @submit.prevent.stop="onTattoosAdd">
          <div class="row">
            <div class="col">
              <div class="form-floating">
                <input type="text" class="form-control" v-model="tattooToAdd.name" required />
                <label for="floatingInput">Название татуировки</label>
              </div>
            </div>
            <div class="col-auto">
              <input class="form-control" type="file" ref="tattoosPictureRef" @change="tattoosAddPictureChange">
            </div>
            <div class="col-auto">
              <img :src="tattooAddImageUrl" style="max-height: 60px;" alt="">
            </div>
          </div>
          <div class="row">
            <div class="col">
              <div class="form-floating">
                <select class="form-select" v-model="tattooToAdd.style" required>
                  <option value="" disabled>Выберите стиль</option>
                  <option :value="s.id" v-for="s in styles" :key="s.id">
                    {{ s.name }}
                  </option>
                </select>
                <label for="floatingInput">Стиль татуировки</label>
              </div>
            </div>
            <div class="col">
              <div class="form-floating">
                <select class="form-select" v-model="tattooToAdd.price" required>
                  <option value="" disabled>Выберите цену</option>
                  <option :value="p.id" v-for="p in prices" :key="p.id">
                    {{ p.name }}
                  </option>
                </select>
                <label for="floatingInput">Цена татуировки</label>
              </div>
            </div>
            <div class="col">
              <div class="form-floating">
                <select class="form-select" v-model="tattooToAdd.tattooArtist" required>
                  <option value="" disabled>Выберите тату мастера</option>
                  <option :value="a.id" v-for="a in tattooArtists" :key="a.id">
                    {{ a.name }}
                  </option>
                </select>
                <label for="floatingInput">Тату мастер</label>
              </div>
            </div>
            <div class="col-auto">
              <button class="btn btn-dark">Добавить</button>
            </div>
          </div>

          <div v-for="item in tattoos" class="tattoos-item" :key="item.id">
            <div class="tattoos-image">
              <img v-if="item.picture" :src="item.picture" style="max-height: 500px; max-width: 500px"
                @click="showImageModal(item.picture)" data-bs-toggle="modal"
                data-bs-target="#imgModal" alt="tattoo" />
            </div>
            <div class="tattoos-info">
              <div class="name">
                {{ item.name }}
              </div>
              <div>
                <b>Стиль:</b> {{ item.style?.name }}
              </div>
              <div>
                <b>Цена:</b> {{ item.price?.name }}
              </div>
              <div>
                <b>Мастер:</b> {{ item.tattooArtist?.name }}
              </div>
            </div>
            <div class="tattoos-buttons">
              <button class="btn btn-dark " @click="onTattooEditClick(item)" data-bs-toggle="modal"
                data-bs-target="#editModal">
                <i class="bi bi-pencil-square"></i>
              </button>
              <button class="btn btn-dark " @click="onTattooRemoveClick(item)">
                <i class="bi bi-x-square-fill"></i>
              </button>
            </div>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.row {
  align-items: center;
  margin-bottom: 10px;
}

.tattoos-item {
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ddd;
  margin-bottom: 5px;
  background-color: #f8f8f8;
  border-radius: 5px;
  display: grid;
  grid-template-columns: 1fr 1fr 0fr;
  gap: 16px;
  align-items: center;
}

.tattoos-item b {
  font-weight: bold;
}

.tattoos-info {
  display: flex;
  flex-direction: column;
}

.tattoos-info .name {
  font-size: 24px;
}

.tattoos-image {
  display: flex;
  align-items: center;
  justify-content: center;

}

.tattoos-buttons {
  display: flex;
  gap: 8px;
  align-items: left;
  justify-content: flex-start;
  /* Кнопки выровнены влево */
}
</style>