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
            <input type="text" id="title" name="title" readonly v-model="diary.title">

            <label for="content">Content:</label>
            <textarea id="content" name="content" readonly v-model="diary.content"></textarea>
            <p>{{ formatDatetime(diary.created_at) }}</p>
          </form>
        </div>

      <div class="right-container">
        <div class="dropdown-container">
          <select class="dropdown" v-model="selectedCharacter">
              <option value="" disabled selected>キャラを選択してね</option>
              <option v-for="(value, key) in AIData" :key="key" :value="key">
                {{ key }}
              </option>
            </select>
            <select class="dropdown" v-model="selectedPersonality" v-if="selectedCharacter">
              <option value="" disabled selected>特徴を選択してね</option>
              <option v-for="(value, key) in AIData[selectedCharacter]" :key="key" :value="key">
                {{ key }}
              </option>
            </select>
      </div>
      <button class="button additional-button" style="margin-bottom: 30px;" :disabled="!selectedCharacter || !selectedPersonality" :style="{ opacity: (!selectedCharacter || !selectedPersonality) ? 0.5 : 1 }" @click="submitForm">
          Additional Button
      </button>

        <div class="comment">
          <h2>Comment List</h2>
          <ul>
              <li v-for="comment in (comments[0] || []).reverse()" :key="comment.comment_id">
                  <p>{{ comment.Select_Character_Role}}</p>
                  <p>{{ comment.Select_Character_Disposition }}</p>
                  <p>{{ comment.content }}</p>
                  <p>{{ formatDatetime(comment.created_at) }}</p>
              </li>
            </ul>
        </div>

      <textarea class="comment" rows="5" readonly v-model="responseText"></textarea>
      </div>
    </div>
    </body>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import AIData from "../assets/AI_data.json"
import axios from "axios";
import { toRaw } from 'vue';
export default {

  name: "Comment",
  components:{
      Header
  },
  data() {
      return {
        diary_id: "",
        diary: [],
        AIData: AIData,
        selectedCharacter: "",
        selectedPersonality: "",
        responseText: "",
        comments: []
      };
  },
  async created() {
    this.diary_id = this.$route.params.diary_id
    try {
        const token = localStorage.getItem("access");

        await Promise.all([this.getDiary(token, diary_id), this.getComments(token, diary_id)]);
  
        } catch (error) {
            console.error("Failed to fetch diaries.");
            console.error(error);
            this.diary = this.sample;
        }
  },
  methods: {
      submitForm() {
          const url = `http://localhost:8000/api/diaries/CommentView/${this.diary_id}`; // 現在は一時的にDBへの保存を経由しない別のAPIを指定
          const token = localStorage.getItem("access"); 
    
          const data = {
            diary_id: this.diary_id,
            Select_Character_Role: this.selectedCharacter,
            Select_Character_Disposition: this.selectedPersonality,
            context: this.AIData[this.selectedCharacter][this.selectedPersonality],
            content: this.diary.content,
          };
    
          const headers = {
            Authorization: `Bearer ${token}`
          };
    
          axios.post(url, data, { headers })
            .then(response => {
              this.responseText = response.data["response"];
              window.location.reload();
            })
            .catch(() => {
              this.responseText = "エラーが発生しました。";
            });
            
        },
      postComment() {
          const url = "http://localhost:8000/api/diaries/CommentView"; 
          const token = localStorage.getItem("access"); 
    
          const data = {
            diary_id: this.diary_id,
            character: this.selectedCharacter,
            personality: this.selectedPersonality,
            context: this.AIData[this.selectedCharacter][this.selectedPersonality],
            content: this.diary.content,
          };
    
          const headers = {
            Authorization: `Bearer ${token}`
          };
    
          axios.post(url, data, { headers })
            .then(response => {
              this.responseText = response.data["response"];
            })
            .catch(() => {
              this.responseText = "エラーが発生しました。";
            });
        },
      formatDatetime(datetime) {
          const date = new Date(datetime);
          const year = date.getFullYear();
          const month = ("0" + (date.getMonth() + 1)).slice(-2);
          const day = ("0" + date.getDate()).slice(-2);
          const hour = ("0" + date.getHours()).slice(-2);
          const minute = ("0" + date.getMinutes()).slice(-2);
          return `${year}-${month}-${day} ${hour}:${minute}`;
        },
      getDiary(token, diary_id) {
        const response = axios.get(`http://localhost:8000/api/diaries/${diary_id}`, {
          headers: {
              'Authorization': `Bearer ${token}`,
          },
        });
        console.log(response.data);
        const rawRes = toRaw(response.data);
        const jsonString = JSON.stringify(rawRes);
        this.diary = JSON.parse(jsonString);
        this.diary.content = this.diary.content.replace(/\\n/g, "\n");
      },
      getComments (token, diary_id) {
        const response = axios.get(`http://localhost:8000/api/diaries/CommentView/${diary_id}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        this.comments = response.data;
        console.log(response.data);
      },

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