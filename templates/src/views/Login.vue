<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-900">
          Login
        </h2>
      </div>
      <div>
        <input v-model="email" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" placeholder="Email" />
        <input v-model="password" class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 focus:z-10 sm:text-sm" type="password" placeholder="Password" />
        <button @click="login" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Login</button>
        <p v-if="loginFailed" class="text-center text-red-500">Login failed.</p>
      </div>
      <div class="text-sm">
        <p class="font-medium text-center">
          Don't have an account? <router-link class="text-indigo-600 hover:text-indigo-500" to="/register">Sign in</router-link>
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
        email: '',
        password: '',
      };
    },
    methods: {
        async login() {
  try {
    const response = await axios.post('http://localhost:8000/api/auth/login/', {
      email: this.email,
      password: this.password,
    });

    localStorage.setItem('access', response.data.access);
    localStorage.setItem('refresh', response.data.refresh);

    this.$router.push('/dashboard');
  } catch (error) {
    console.error('Login failed.');
    console.error(error.response.data);
  }
},
    },
  };
  </script>
  