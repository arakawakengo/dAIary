<template>
    <div class="header">
        <div class="title">dAIary</div>
        <div class="nav-links">
            <router-link to="/dashboard">Home</router-link>
            <router-link to="/diary-create">Post Diary</router-link>
            <router-link to="/profile">Profile</router-link>
            <router-link to="/">Sign out</router-link>
        </div>
    </div>
</template>


<script>
export default {
    name: "Header",
}
</script>

<style>
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: #333;
    color: white;
}

.header .title {
    font-size: 2em;
}

.header .nav-links {
    display: flex;
}

.header .nav-links a {
    color: white;
    text-decoration: none;
    margin-left: 10px;
}

.header .nav-links a:hover {
    color: #ddd;
}

.router-link-exact-active {
    color: #ff6347;
}
</style>
