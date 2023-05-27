<template>
  <div>
    <Header />
    <div class="diary-create">
    <div class="create-form">
      <div class="create-heading">
        <h2>Write Diary</h2>
      </div>
      <div class="form-fields">
        <label for="title" class="sr-only">Title:</label>
        <input
          v-model="title"
          id="title"
          type="text"
          class="title-input"
          placeholder="Title"
          required
        />
        <label for="content" class="sr-only">Content:</label>
        <textarea
          v-model="content"
          id="content"
          class="text-input"
          placeholder="Content"
          required
        ></textarea>
        <button
          @click="createDiary"
          class="create-button"
        >
          Post Diary
        </button>
      </div>
    </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Header from "../components/Header.vue"
export default {
  components: {
    Header
  },
  data() {
    return {
      title: "",
      content: "",
    };
  },
  methods: {
    async createDiary() {
      try {
        const token = localStorage.getItem("access");
        await axios.post("http://localhost:8000/api/diaries/", {
          title: this.title,
          content: this.content,
        }, {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        this.$router.push("/dashboard");
      } catch (error) {
        console.error("Failed to create diary.");
        console.error(error.response.data);
      }
    },
  },
};
</script>

<style scoped>
.diary-create {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  background-color: #f7fafc;
  padding: 3rem;
}

.create-form {
  background-color: #ffffff;
  padding: 2rem;
  border-radius: 0.5rem;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  width: 80%;
  height: 100%;
  margin-top: 2rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.create-heading {
  text-align: center;
  margin-bottom: 1.5rem;
}

.create-heading h2 {
  font-size: 1.5rem;
  font-weight: bold;
}

.form-fields {
  display: flex;
  flex-direction: column;
}

.title-input,
.text-input {
  border: 1px solid #cbd5e0;
  border-radius: 0.25rem;
  padding: 0.5rem;
  margin-bottom: 1rem;
  width: 100%;
}

.text-input{
  height: 500px;
  resize: vertical;
}

.create-button {
  background-color: #000000;
  color: #fff;
  border: none;
  border-radius: 0.25rem;
  padding: 0.5rem 1rem;
  cursor: pointer;
  font-size: 1rem;
  font-weight: bold;
}

.create-button:hover {
  background-color: #333;
}

.Header {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 999;
}
</style>