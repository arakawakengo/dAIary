<template>
  <div>
    <Header />
    <h1>Dashboard</h1>
    <p>Welcome, you are logged in!</p>
    <div class="diary-list">
      <h2>Diary List</h2>
      
      <ul>
          <li v-for="diary in (diary_list[0] || []).reverse()" :key="diary.diary_id">
            <router-link :to="`/comment/${diary.diary_id}`">
              <p>{{ diary.diary_id }}</p>
              <h3>{{ diary.title }}</h3>
              <p>{{ diary.content }}</p>
              <p>{{ formatDatetime(diary.created_at) }}</p>
            </router-link>
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
      const response = await axios.get("http://localhost:8000/api/diaries/", {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      });
      this.diary_list.push(response.data.diary_list);
      this.diary_list[0].forEach(diary => {
        diary.content = diary.content.replace(/\\n/g, "\n");
      });      
      console.log(this.diary_list[0]);
    } catch (error) {
      console.error("Failed to fetch diaries.");
      console.error(error);
    }
  },
  methods: {
    formatDatetime(datetime) {
      const date = new Date(datetime);
      const year = date.getFullYear();
      const month = ("0" + (date.getMonth() + 1)).slice(-2);
      const day = ("0" + date.getDate()).slice(-2);
      const hour = ("0" + date.getHours()).slice(-2);
      const minute = ("0" + date.getMinutes()).slice(-2);
      return `${year}-${month}-${day} ${hour}:${minute}`;
    },
  },
};
  </script>

<style scoped>
h1 {
  color: #333;
  font-size: 2em;
  margin-bottom: 0.5em;
}

p {
  color: #666;
  font-size: 1.2em;
}

.diary-list {
  margin-top: 2em;
}

.diary-list h2 {
  color: #333;
  font-size: 1.8em;
  margin-bottom: 1em;
}

.diary-list ul {
  list-style-type: none;
  padding: 0;
}

.diary-list li {
  margin-bottom: 1em;
  border: 1px solid #ddd;
  padding: 1em;
  border-radius: 5px;
  background-color: #f9f9f9;
}

.diary-list h3 {
  color: #444;
  font-size: 1.5em;
  margin-bottom: 0.5em;
}

.diary-list p {
  color: #666;
  font-size: 1.2em;
}
</style>
