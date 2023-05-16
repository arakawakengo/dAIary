<template>
    <div>
      <Header />
      <h1>Dashboard</h1>
      <p>Welcome, you are logged in!</p>
      <button @click="sendRequest">Send request</button>
      <p v-if="requestSuccessful">Request was successful!</p>
      <p v-else-if="requestFailed">Request failed.</p>
    </div>
  </template>
  
  <script>
    import axios from 'axios';
    import Header from "../components/Header.vue"

  export default {
    name: 'Dashboard',
    components: {
        Header
    },
    data() {
      return {
        requestSuccessful: false,
        requestFailed: false,
      };
    },
    methods: {
      async sendRequest() {
          const token = localStorage.getItem('access');
          console.log(token)
          const refresh = localStorage.getItem('refresh');
          try {
            const response = await axios.get('http://localhost:8000/api/diaries/', {
              headers: { 'Authorization': `Bearer ${token}` }
            });
            this.requestSuccessful = true;
            this.requestFailed = false;
            console.log(response)
          } catch (error) {
            if (error.response.status === 401){
              const response = await axios.post('http://localhost:8000/api/auth/refresh/', {
                refresh: refresh
              });
              localStorage.setItem('access', response.data.access);
              return this.sendRequest();
            } else {
              console.error(error.response.data);
              this.requestFailed = true;
              this.requestSuccessful = false;
            }
        }
      }
    }
  };
  </script>
  