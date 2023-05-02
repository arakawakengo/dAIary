<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Create Diary
        </h2>
      </div>
      <div>
        <label for="title" class="sr-only">Title:</label>
        <input
          v-model="title"
          id="title"
          type="text"
          class="appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Title"
          required
        />
        <label for="content" class="sr-only">Content:</label>
        <textarea
          v-model="content"
          id="content"
          class="mt-2 h-64 appearance-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm"
          placeholder="Content"
          required
        ></textarea>
        <button
          @click="createDiary"
          class="mt-4 group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
        >
          Submit
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
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
        this.$router.push("/diary-list");
      } catch (error) {
        console.error("Failed to create diary.");
        console.error(error.response.data);
      }
    },
  },
};
</script>


