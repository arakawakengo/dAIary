<template>
    <div class="upload">
    <Header/>
        <head>
        <meta charset="UTF-8">
        </head>
      <body>
        <div class="container">
          <div class="left-container">
            <form class="form">
              <label for="title">Title:</label>
              <input type="text" id="title" name="title" readonly>

              <label for="content">Content:</label>
              <textarea id="content" name="content" readonly></textarea>
            </form>
          </div>

        <div class="right-container">
          <div class="dropdown-container">
            <select class="dropdown" v-model="selectedCharacter">
                <option value="" disabled selected>キャラを選択してね</option>
                <option v-for="(value, key) in jsonData" :key="key" :value="key">
                  {{ key }}
                </option>
              </select>
              <select class="dropdown" v-model="selectedPersonality" v-if="selectedCharacter">
                <option value="" disabled selected>特徴を選択してね</option>
                <option v-for="(value, key) in jsonData[selectedCharacter]" :key="key" :value="key">
                  {{ key }}
                </option>
              </select>
        </div>
        <button class="button additional-button" style="margin-bottom: 30px;" :disabled="!selectedCharacter || !selectedPersonality" @click="submitForm">
            Additional Button
        </button>
        <textarea class="comment" rows="5" readonly v-model="responseText"></textarea>
        </div>
      </div>
      </body>
    </div>
</template>

<script>
import Header from "@/components/Header.vue";
import jsonData from '@/assets/AI_data.json';
import axios from "axios";


export default {
    name: "ComMent",
    components:{
        Header
    },
    data() {
        return {
          jsonData: jsonData,
          selectedCharacter: "",
          selectedPersonality: "",
          responseText: ""
        };
    },
    methods: {
        submitForm() {
            const url = "http://localhost:8000/api/comment/"; // 現在は一時的にDBへの保存を経由しない別のAPIを指定
            const token = localStorage.getItem("access"); 
      
            const data = {
              context : this.jsonData[this.selectedCharacter][this.selectedPersonality],
              diary_text: "10時ごろに宅配便で目がさめる。ヨーグルトとビスケットを食べて二度寝する。起きたら16時だった。\nやんなきゃいけないことはたくさんあるけどやる気しないなあ。\n \
              部屋で寝てると気分が沈んでいくけど、外を歩いているときだけは少し前向きになる。でも部屋に戻るとまただめだ。\n22時くらいから少しマシになってきて本を読んだりする。あとパネポン。"
            };
      
            const headers = {
              Authorization: `Bearer ${token}`
            };
      
            axios.post(url, data, { headers })
              .then(response => {
                this.responseText = JSON.stringify(response.data["response"]);
              })
              .catch(() => {
                this.responseText = "エラーが発生しました。";
              });
          }
    }

};
</script>


<style scoped>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}

.container {
  height: 100vh;
  display: flex;
}

.left-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.right-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.dropdown-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px; /* Adjusted margin */
}

.dropdown {
  margin-bottom: 20px;
  padding: 10px 20px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  background-color: #f1f1f1;
}

.additional-button {
  padding: 15px 30px; /* Increased padding */
  font-size: 18px; /* Increased font size */
  border: none;
  border-radius: 4px;
  background-color: #f1f1f1;
  width: 100%; /* Make button wider */
  max-width: 300px; /* Set a maximum width */
  text-align: center;
  box-sizing: border-box;
}

.comment {
  margin-top: auto;
  margin-bottom: 20px;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 92%;
  max-width: 600px;
  resize: vertical;
  background-color: #f1f1f1;
  pointer-events: none;
}

.form {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 90%;
  max-width: 600px;
}

label {
  font-size: 18px;
  margin-top: 10px;
}

input[type="text"],
textarea {
  padding: 5px;
  margin-top: 5px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  resize: vertical;
  box-sizing: border-box;
  padding: 10px;
  font-family: Arial, sans-serif;
  background-color: #f1f1f1;
  pointer-events: none;
}

input[type="text"] {
  height: 70px;
}

textarea {
  height: 550px;
}
</style>