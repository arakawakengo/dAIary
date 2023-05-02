<template>
    <div>
      <h2>Diary List</h2>
      <ul>
        <li v-for="diary in diaries" :key="diary.id">
          <h3>{{ diary.title }}</h3>
          <p>{{ diary.content }}</p>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  export default {
    data() {
      return {
        diaries: [],
      };
    },
    async created() {
      try {
        const token = localStorage.getItem("access");
        const response = await axios.get("/api/diaries/", {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        this.diaries = response.data;
      } catch (error) {
        console.error("Failed to fetch diaries.");
        console.error(error.response.data);
      }
    },
  };
  </script>
  