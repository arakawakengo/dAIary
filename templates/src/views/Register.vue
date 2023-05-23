<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Register
        </h2>
      </div>
      <div>
        <p v-if="errorMessage" class="text-center text-red-500">{{ errorMessage }}</p>
        <form @submit.prevent="register">
          <label for="username" class="sr-only">Username:</label>
          <input type="text" id="username" v-model="username" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Username" required />
          
          <label for="email" class="sr-only">Email:</label>
          <input type="email" id="email" v-model="email" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Email" required />

          <label for="password" class="sr-only">Password:</label>
          <input type="password" id="password" v-model="password" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Password" required />
    
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-gray-800 hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Register</button>
        </form>
      </div>
      <div class="text-sm">
        <p class="font-medium text-center">
          Already have an account? <router-link class="text-indigo-600 hover:text-indigo-500" to="/">Log in</router-link>
        </p>
      </div>
    </div>
  </div>
</template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        username: '',
        password: '',
        email: '',
        errorMessage: '',
      };
    },
    methods: {
        async register() {
  try {
    await axios.post('http://localhost:8000/api/auth/register/', {
      username: this.username,
      email: this.email,
      password: this.password,
    });
    setTimeout(() => {
          this.$router.push({ name: 'Login' })
        }, 1000)
  } catch (error) {
    console.error('Registration failed.');
    console.error(error.response.data);
    this.errorMessage = error.response.data.username[0];
  }
},
    },
  };
  </script>
  

  