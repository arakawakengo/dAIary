<template>
    <div>
      <Header />
      <h1>Dashboard</h1>
      <p>Welcome, you are logged in!</p>
    </div>
  </template>
  
  <script>
  import Header from "../components/Header.vue"
  export default {
    name: 'Dashboard',
    components: {
        Header
    }
  };
  </script>
  