<script setup>
import axios from "axios";
import { computed, onBeforeMount, ref } from "vue";
import _ from "lodash";
import Cookies from "js-cookie";

const tattooArtists = ref([]);
const tattooStudios = ref([]);
const tattooArtistPictureRef = ref();
const tattooArtistAddImageUrl = ref();
const tattooArtistEditPictureRef = ref(); // Используйте только для редактирования
const tattooArtistEditImageUrl = ref();
const selectedImage = ref("");

const tattooArtistToAdd = ref({});
const tattooArtistToEdit = ref({});

async function onTattooArtistsAdd() {
    const formData = new FormData();
    formData.append("picture", tattoosPictureRef.value.files[0]);
    formData.set("name", tattooArtistToAdd.value.name);
    formData.set("tattooStudio", tattooArtistToAdd.value.tattooStudio);

    await axios.post("/api/tattooArtists/", formData, {
        headers: {
            "Content-Type": "multipart/form-data",
        },
    });
    await fetchTattooArtist(); // переподтягиваю
}

async function fetchTattooArtist() {
    const r = await axios.get("/api/tattooArtists/");
    tattooArtists.value = r.data;
}
async function fetchTattooStudios() {
    const r = await axios.get("/api/tattooStudios/");
    console.log(r.data);
    tattooStudios.value = r.data;
}

async function onTattooArtistsRemoveClick(tattooArtists) {
    await axios.delete(`/api/tattooArtists/${tattooArtists.id}/`);
    await fetchTattooArtist(); // переподтягиваю
}

async function onTattooArtistsEditClick(tattooArtist) {
    tattooArtistToEdit.value = { ...tattooArtist, tattooStudio: tattooArtist.tattooStudio.id };
    tattooArtistEditImageUrl.value = tattooArtist.picture;
}

async function onTattooArtistsUpdate() {
    const formData = new FormData();

    // Добавляем изображение, если оно было загружено для редактирования
    if (tattooArtistToEdit.value.picture) {
        formData.append("picture", tattooArtistToEdit.value.picture);
    }

    formData.set("name", tattooArtistToEdit.value.name);
    formData.set("tattooStudio", tattooArtistToEdit.value.tattooStudio);

    await axios.put(
        `/api/tattooArtists/${tattooArtistToEdit.value.id}/`,
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );
    await fetchTattooArtist(); // переподтяг
}

async function tattooArtistsEditPictureChange(event) {
    const file = event.target.files[0];
    if (file) {
        tattooArtistEditImageUrl.value = URL.createObjectURL(file);
        tattooArtistToEdit.value.picture = file; // Сохраняем файл в tattooToEdit
    }
}

async function tattooArtistsAddPictureChange() {
    tattooArtistAddImageUrl.value = URL.createObjectURL(
        tattooArtistPictureRef.value.files[0]
    );
}

async function showImageModal(imageUrl) {
    selectedImage.value = imageUrl;
}

onBeforeMount(async () => {
    axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
    await fetchTattooStudios();
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
                        {{tattooArtistToEdit}}
                        <div class="row">
                            <div class="col">
                                <div class="form-floating">
                                    <input type="text" class="form-control" v-model="tattooArtistToEdit.name"
                                        required />
                                    <label for="floatingInput">Имя тату мастера</label>
                                </div>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-auto">
                                <input class="form-control" type="file" ref="tattooArtistEditPictureRef"
                                    @change="tattooArtistsEditPictureChange" />
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-auto">
                                <div class="form-floating">
                                    <select class="form-select" v-model="tattooArtistToEdit.tattooStudio" required>
                                        <option value="" disabled>Выберите тату студию</option>
                                        <option :value="s.id" v-for="s in tattooStudios" :key="s.id">
                                            {{ s.name }}
                                        </option>
                                    </select>
                                    <label for="floatingInput">Тату студия</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Закрыть
                        </button>
                        <button type="button" class="btn btn-dark" data-bs-dismiss="modal"
                            @click="onTattooArtistsUpdate">
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
                        <h1 class="modal-title fs-5" id="imgModalLabel">Тату мастер</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <div class="row">
                            <div class="col">
                                <img :src="selectedImage" alt="" style="max-width: 100%; height: auto" />
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
                <form @submit.prevent.stop="onTattooArtistsAdd">
                    <div class="row">
                        <div class="col">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="tattooArtistToAdd.name" required />
                                <label for="floatingInput">Имя тату мастера</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <input class="form-control" type="file" ref="tattooArtistsPictureRef"
                                @change="tattooArtistsAddPictureChange" />
                        </div>
                        <div class="col-auto">
                            <div class="form-floating">
                                <select class="form-select" v-model="tattooArtistToAdd.tattooStudio" required>
                                    <option value="" disabled>Выберите тату студию</option>
                                    <option :value="s.id" v-for="s in tattooStudios" :key="s.id">
                                        {{ s.name }}
                                    </option>
                                </select>
                                <label for="floatingInput">Тату студия</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <button class="btn btn-dark">Добавить</button>
                        </div>
                    </div>

                    <div>
                        <div v-for="item in tattooArtists" :key="item.id" class="tattoo-artist-container">
                            <div class="tattoo-artist-image">
                                <img v-if="item.picture" :src="item.picture" @click="showImageModal(item.picture)"
                                    data-bs-toggle="modal" data-bs-target="#imgModal" alt="tattoo">
                            </div>
                            <div class="tattoo-artist-info">
                                <p class="artist-name">{{ item.name }}</p>
                                <p >Тату студия: {{ item.tattooStudio?.name }}</p>
                            </div>
                            <div class="tattoo-artist-actions">
                                <button class="btn btn-dark" @click="onTattooArtistsEditClick(item)"
                                    data-bs-toggle="modal" data-bs-target="#editModal">
                                    <i class="bi bi-pencil-square"></i>
                                </button>
                                <button class="btn btn-dark" @click="onTattooArtistsRemoveClick(item)">
                                    <i class="bi bi-x-square-fill"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<style lang="scss" scoped>
.tattoo-artist-container {
    display: flex;
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ddd;
    margin-bottom: 5px;
    background-color: #f8f8f8;
    border-radius: 5px;
    gap: 16px;
}

.tattoo-artist-image {
    max-width: 250px;
    /* Adjust as needed */
}

.tattoo-artist-image img {
    
    max-width: 100%;
    object-fit: cover;
}

.tattoo-artist-info {
    flex: 1;
    /* Takes up available space */
}

.artist-name {
    margin-bottom: 5px;
    font-size: 24px;
}



.tattoo-artist-actions {
    display: flex;
    gap: 8px;
}
</style>
