<script setup>
import axios from "axios";
import { computed, onBeforeMount, ref } from "vue";
import _ from "lodash";
import Cookies from "js-cookie";


const tournaments = ref({});
const rankSignificance = ref({});
const participantList = ref({});
const isAuthenticated = computed(() => {
  return !!Cookies.get("csrftoken"); // или другой ваш маркер авторизации, например access_token
});

const searchQuery = ref("");
const selectedMonth = ref("");

// Список месяцев
const months = [
  { value: "", label: "Все месяцы" },
  { value: "01", label: "Январь" },
  { value: "02", label: "Февраль" },
  { value: "03", label: "Март" },
  { value: "04", label: "Апрель" },
  { value: "05", label: "Май" },
  { value: "06", label: "Июнь" },
  { value: "07", label: "Июль" },
  { value: "08", label: "Август" },
  { value: "09", label: "Сентябрь" },
  { value: "10", label: "Октябрь" },
  { value: "11", label: "Ноябрь" },
  { value: "12", label: "Декабрь" },
];

const filteredTournaments = computed(() => {
  return Object.values(tournaments.value).filter((item) => {
    const search = searchQuery.value.toLowerCase();

    const allFields = [
      item.name,
      item.level,
      item.age_category,
      item.location,
      item.start_date,
      item.end_date,
      item.registration_deadline
    ]
      .join(" ")
      .toLowerCase();

    const nameMatch = allFields.includes(search);

    const monthMatch = selectedMonth.value
      ? new Date(item.start_date).toISOString().slice(5, 7) === selectedMonth.value
      : true;

    return nameMatch && monthMatch;
  });
});



async function fetchTournamentst() {
  const r = await axios.get("/api/tournaments/"); // Полный URL
  console.log(r.data);  // Здесь может вывалиться ошибка, если r.data undefined
  tournaments.value = r.data;

}
async function fetchRankSignificance() {
  const r = await axios.get("/api/rankSignificances/");
  console.log(r.data);
  rankSignificance.value = r.data;
}

async function fetchParticipantList() {
  const r = await axios.get("/api/participantLists/"); // Полный URL
  console.log(r.data);  // Здесь может вывалиться ошибка, если r.data undefined
  participantList.value = r.data;

}

onBeforeMount(async () => {
  axios.defaults.headers.common["X-CSRFToken"] = Cookies.get("csrftoken");
  await fetchTournamentst();
  await fetchRankSignificance();

});

</script>

<template>
  <div class="tournament-list container mt-4">
    <div class="d-flex mb-3 gap-3 flex-wrap">
  <input
    v-model="searchQuery"
    type="text"
    class="form-control w-auto"
    placeholder="Поиск по названию"
  />
  <select v-model="selectedMonth" class="form-select w-auto">
    <option v-for="month in months" :value="month.value" :key="month.value">
      {{ month.label }}
    </option>
  </select>
</div>

    <h2 class="mb-4 text-left">Список турниров</h2>

    <div
  v-for="item in filteredTournaments"
  :key="item.id"
  class="card mb-4 shadow-sm p-3 tournament-card"
>

      <div class="row align-items-center">
        <!-- Левая часть: Информация -->
        <div class="col-md-8">
          <h5 class="fw-bold">{{ item.name }}</h5>
          <p><strong>Уровень:</strong> {{ item.level }}</p>
          <p><strong>Возрастная категория:</strong> {{ item.age_category }}</p>
          <p><strong>Место:</strong> {{ item.location }}</p>
          <p><strong>Дата начала:</strong> {{ item.start_date }}</p>
          <p><strong>Дата окончания:</strong> {{ item.end_date }}</p>
          <p><strong>Срок подачи заявок:</strong> {{ item.registration_deadline }}</p>
        </div>

        <!-- Правая часть: Разрядная значимость и кнопки -->
        <div class="col-md-4 text-end">
          <p class="text-primary">
  <strong>Разрядная значимость:</strong><br />
  {{
    rankSignificance.find(rs => rs.tournament.id === item.id)?.rank_level || '—'
  }}
</p>



          <button
  class="btn btn-primary mb-2 w-100"
  :disabled="!isAuthenticated"
>
  Подать заявку
</button>
<small v-if="!isAuthenticated" class="text-muted">
  Для подачи заявки необходимо войти
</small>

          <button class="btn btn-outline-secondary w-100">
            Список участников
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<style lang="scss" scoped>

</style>