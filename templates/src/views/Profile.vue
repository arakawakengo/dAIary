<template>
<body>
    <Header />
    <main>
        <div id="profile">
            <div1>
                <img src="https://via.placeholder.com/100x100" alt="profile picture">
                <button id="change-icon">アイコン変更</button>
            </div1>

            <div2>
                <p>john.doe@example.com</p>
                <label for="username">ユーザーネーム：</label>
                <input type="text" id="username" name="username"><br>
                <button id="update-password-btn">パスワード変更</button>
                <button id="update-username-btn">ユーザーネーム変更</button>
            </div2>
        </div>

        <div class="diary">
            <h2>My日記</h2>
            <ul>
                <li>日記1</li>
                <li>日記2</li>
                <li>日記3</li>
            </ul>
        </div>
    </main>
    <footer>
        <p>&copy; 2023 dAIary</p>
    </footer>
</body>
</template>

<script>
import Header from "../components/Header.vue"
export default {
    name: "Profile",
    components: {
        Header
    }
}
</script>

<style scoped>
body {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}
header {
    background-color: #F2F2F2;
    padding: 10px;
    display: flex;
    align-items: center;
}
#logo {
    font-size: 32px;
    font-weight: bold;
    margin: 0;
    padding: 0;
    margin-right: 50px;
}
#menu {
    display: flex;
    flex-grow: 1;
    justify-content: flex-end;
}
#menu a {
    margin-right: 20px;
    color: #333;
    text-decoration: none;
    font-size: 18px;
    font-weight: bold;
}
#profile {
    display: flex;
    align-items: center;
    margin-top: 50px;
    margin-left: 50px;
}


#profile img {
    width: 100px;
    height: 100px;
    border-radius: 50%;
    margin-right: 20px;
}

#profile div1 {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

#profile div2 {
    display: flex;
    flex-direction: column;
    justify-content: center;
}
#profile h2 {
    margin: 0;
    padding: 0;
    font-size: 24px;
    font-weight: bold;
    color: #333;
}
#profile p {
    margin: 0;
    padding: 0;
    font-size: 18px;
    color: #666;
}
#diary {
    margin-top: 50px;
    margin-left: 50px;
    margin-right: 50px;
}
#diary textarea {
    width: 100%;
    height: 200px;
    border: 1px solid #ccc;
    padding: 10px;
    font-size: 18px;
    resize: none;
}
#diary button {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 10px;
    float: right;
}
#diary button:hover {
    background-color: #3E8E41;
}
.diary {
    background-color: #F2F2F2;
    width: 100%;
}
.diary h2 {
    font-size: 15px;
    margin-top: 10px;
    margin-left: 10px;
}
.diary ul {
    list-style: none;
    margin: 0;
    padding: 0;
}
.diary li {
    margin: 15px;
    width: 75%;
    height: 200px;
    padding: 10px;
    background-color: white;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
#profile button {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
    margin-top: 10px;
    margin-left: 20px;
}

#profile button:hover {
    background-color: #3E8E41;
}
</style>