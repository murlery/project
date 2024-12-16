<script setup>
import axios from "axios";
import { computed, onBeforeMount, ref } from "vue";
import _ from "lodash";
import Cookies from "js-cookie";

const tattooStudios = ref([]);

const tattooStudioToAdd = ref({});
const tattooStudioToEdit = ref({});

async function onTattooStudiosAdd() {
    await axios.post("/api/tattooStudios/", {
        ...tattooStudioToAdd.value,
    });
    await fetchTattooStudios(); // переподтягиваю
    tattooStudioToAdd.value = {};
}

async function fetchTattooStudios() {
    const r = await axios.get("/api/tattooStudios/");
    console.log(r.data);
    tattooStudios.value = r.data;
}


async function onTattooStudiosRemoveClick(tattooStudios) {
    await axios.delete(`/api/tattooStudios/${tattooStudios.id}/`);
    await fetchTattooStudios(); // переподтягиваю
}

async function onTattooStudiosEditClick(tattooStudios) {
    tattooStudioToEdit.value = { ...tattooStudios };
}

async function onTattooStudiosUpdate() {
    await axios.put(`/api/tattooStudios/${tattooStudioToEdit.value.id}/`, {
        ...tattooStudioToEdit.value,
    });
    await fetchTattooStudios(); // переподтягиваю
}

onBeforeMount(async () => {
    axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
    await fetchTattooStudios();
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
                                    <input type="text" class="form-control" v-model="tattooStudioToEdit.name" required />
                                    <label for="floatingInput">Тату студия</label>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">
                            Закрыть
                        </button>
                        <button type="button" class="btn btn-dark" data-bs-dismiss="modal" @click="onTattooStudiosUpdate">
                            Сохранить изменения
                        </button>
                    </div>
                </div>
            </div>
        </div>

        <div>
            <div class="p-2">
                <form @submit.prevent.stop="onTattooStudiosAdd">
                    <div class="row">
                        <div class="col-auto">
                            <div class="form-floating">
                                <input type="text" class="form-control" v-model="tattooStudioToAdd.name" required />
                                <label for="floatingInput">Тату студия</label>
                            </div>
                        </div>
                        <div class="col-auto">
                            <button class="btn btn-dark">Добавить</button>
                        </div>
                    </div>

                    <div v-for="item in tattooStudios" class="tattooStudio-item" :key="item.id">
                        <div>{{ item.name }}</div>
                        <button class="btn btn-dark" @click="onTattooStudiosEditClick(item)" data-bs-toggle="modal"
                            data-bs-target="#editModal">
                            <i class="bi bi-pencil-square"></i>
                        </button>
                        <button class="btn btn-dark" @click="onTattooStudiosRemoveClick(item)">
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

.tattooStudio-item {
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

.tattooStudio-item b {
    font-weight: bold;
}
</style>
