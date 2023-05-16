<template>
  <div>
    <Header />
    <h1>Dashboard</h1>
    <p>Welcome, you are logged in!</p>
    <div class="diary-list">
      <h2>Diary List</h2>
      <div v-for="diary in diary_list" :key="diary.id">
      {{diary}}
      </div>
      <ul>
          <li v-for="diary in diary_list" :key="diary.id">
          <h3>{{ diary.title }}</h3>
          <p>{{ diary.content }}</p>
          <p>response</p>
        </li>
      </ul>
    </div>
  </div>

  </template>
  
<script>
import Header from "../components/Header.vue"
import axios from "axios";
export default {
  name: 'Dashboard',
  components: {
      Header
  },
  data() {
    return {
      diary_list: [],
    };
  },
  async created() {
    try {
      const token = localStorage.getItem("access");
      const response = axios.get("http://localhost:8000/api/diaries/", {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      this.diary_list = response.data;
      console.log(this.diary_list)
    } catch (error) {
      console.error("Failed to fetch diaries.");
      console.error(error.response.data);
    }
  },
};
  </script>