<script setup>
import axios from "axios";
import { computed, onBeforeMount, ref } from "vue";
import _ from "lodash";
import Cookies from "js-cookie";

const tattoos = ref([]);
const styles = ref([]);
const prices = ref([]);
const tattooArtists = ref([]);

const styleToAdd = ref({});
const styleToEdit = ref({});

async function onStylesAdd() {
    await axios.post("/api/styles/", {
        ...styleToAdd.value,
    });
    await fetchStyles(); // переподтягиваю
    styleToAdd.value = {};
}
async function onPricesAdd() {
    await axios.post("/api/prices/", {
        ...priceToAdd.value,
    });
    await fetchPrices(); // переподтягиваю
    priceToAdd.value = {};
}
async function onTattooArtistsAdd() {
    await axios.post("/api/tattooArtists/", {
        ...tattooArtistToAdd.value,
    });
    await fetchTattooArtist(); // переподтягиваю
    tattooArtistToAdd.value = {};
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

async function onStylesRemoveClick(styles) {
    await axios.delete(`/api/styles/${styles.id}/`);
    await fetchStyles(); // переподтягиваю
}

async function onStylesEditClick(styles) {
    styleToEdit.value = { ...styles };
}

async function onStylesUpdate() {
    await axios.put(`/api/styles/${styleToEdit.value.id}/`, {
        ...styleToEdit.value,
    });
    await fetchStyles(); // переподтягиваю
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
                            <div class="col-auto">
                                <div class="form-floating">
                                    <div class="form-floating">
                                        <input type="text" class="form-control" v-model="styleToEdit.name" required />
                                        <label for="floatingInput">Название стиля</label>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Закрыть
                        </button>
                        <button type="button" class="btn btn-dark" data-bs-dismiss="modal" @click="onStylesUpdate">
                            Сохранить изменения
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <div class="p-2">
                <form @submit.prevent.stop="onStylesAdd">
                    <div class="row">
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="styleToAdd.name" required />
                                <label for="floatingInput">Название стиля</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <button class="btn btn-dark">Добавить</button>
                        </div>
                    </div>

                    <div v-for="item in styles" class="style-item" :key="item.id">
                        <div>{{ item.name }}</div>
                        <button class="btn btn-dark" @click="onStylesEditClick(item)" data-bs-toggle="modal"
                            data-bs-target="#editModal">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-dark" @click="onStylesRemoveClick(item)">
                            <i class="bi bi-x-square-fill"></i>
                        </button>
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

.style-item {
    align-items: center;
    padding: 10px;
    border-bottom: 1px solid #ddd;
    margin-bottom: 5px;
    background-color: #f8f8f8;
    border-radius: 5px;
    display: grid;
    grid-template-columns: 1fr auto auto auto;
    gap: 16px;
    justify-content: space-between;
    align-items: center;
}

.style-item b {
    font-weight: bold;
}
</style>
