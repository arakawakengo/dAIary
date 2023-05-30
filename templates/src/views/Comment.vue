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
            <div id="title" name="title" v-html="diary.title"></div>
            <label for="content">Content:</label>
            <p id="content" name="content" v-html="diary.content"></p>
            <p>{{ formatDatetime(diary.created_at) }}</p>
          </form>
          <button class="button delete-button" style="margin-bottom: 15px;" v-on:click="pushedDelete = true">
            Delete diary
          </button>
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
      <button class="button additional-button" style="margin-bottom: 15px;" :disabled="!selectedCharacter || !selectedPersonality" :style="{ opacity: (!selectedCharacter || !selectedPersonality) ? 0.5 : 1 }" @click="submitForm">
          Receive comment
      </button>

      <p v-if="beGeneratingComment" style="margin-bottom: 15px;" >AIがコメントを生成中です <span>{{ ellipsis }}</span> </p>
      <p v-if="responseText && !beGeneratingComment" style="margin-bottom: 15px;" >{{ responseText }}</p>
      

      
      <h2>Comment List</h2>
      <div class="comment_container">
        <ul>
            <li v-for="comment in (comments || [])" :key="comment.commentID">
              <div class="comment">
                <p>{{ comment.content }}</p>
                <p>{{ comment.Select_Character_Disposition_ID }}{{ comment.Select_Character_Role_ID }}より</p>
                <p>{{ formatDatetime(comment.created_at) }}</p>
              </div>
            </li>
            <li v-if="comments.length==0">
              <p>コメントがありません</p>
            </li>
        </ul>
      </div>


      </div>
    </div>
    <transition name="modal">
      <div class="modal-mask" v-if="pushedDelete">
        <div class="modal">
          <p>日記を削除してもいいですか？</p>
          <button class="modal-button" @click="deleteDiary">OK</button>
          <button class="modal-button" v-on:click="pushedDelete = false">NG</button>
        </div>
      </div>
    </transition>
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
        comments: [],
        beGeneratingComment: false,
        ellipsis: '',
        pushedDelete: false,
      };
  },
  async created() {
    this.diary_id = this.$route.params.diary_id
    try {
        const token = localStorage.getItem("access");
        await Promise.all([this.getDiary(token, this.diary_id), this.getComments(token, this.diary_id)]);
    } catch (error) {
        console.error("Failed to fetch diaries.");
        console.error(error);
        this.diary = this.sample;
    }
  },
  methods: {
      submitForm() {
          this.beGeneratingComment = true;

          var dotCount = 0;
          setInterval(() => {
            dotCount = (dotCount + 1) % 4;
            this.ellipsis = '.'.repeat(dotCount);
        }, 500);

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
              this.$router.go({path: this.$router.currentRoute.path, force: true})
              this.responseText = response.data["response"];
            })
            .catch(() => {
              this.beGeneratingComment = false;
              this.responseText = "エラーが発生しました。もう一度試みてください。";
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
    async getDiary(token, diary_id) {
        const response = await axios.get(`http://localhost:8000/api/diaries/${diary_id}/`, {
          headers: {
              'Authorization': `Bearer ${token}`,
          },
        });
        const rawRes = toRaw(response.data);
        const jsonString = JSON.stringify(rawRes);
        this.diary = JSON.parse(jsonString);
        this.diary.content = this.diary.content.replace(/\\n/g, "\n");
      },
        
    async getComments (token, diary_id) {
        const response = await axios.get(`http://localhost:8000/api/diaries/CommentView/${diary_id}`, {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        this.comments = response.data.diary_comment_list;
      },
    async deleteDiary() {
        const token = localStorage.getItem("access");
        await axios.delete(`http://localhost:8000/api/diaries/${this.diary_id}/`, {
          headers: {
              'Authorization': `Bearer ${token}`,
          },
        });
        this.$router.push('/calendar');
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
align-items: flex-start;
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
background-color: #F1F1F1;
}
.additional-button {
padding: 15px 30px; /* Increased padding */
font-size: 18px; /* Increased font size */
border: none;
border-radius: 4px;
background-color: #F1F1F1;
width: 100%; /* Make button wider */
max-width: 300px; /* Set a maximum width */
text-align: center;
box-sizing: border-box;
}
.delete-button {
padding: 5px 10px; 
font-size: 13px;
border: none;
border-radius: 1px;
background-color: #F1F1F1;
width: 100%; 
max-width: 200px; 
text-align: center;
color:  red;
}
.comment_container {
margin-top: auto;
margin-bottom: 20px;
padding: 10px;
font-size: 16px;
border: 1px solid #ccc;
border-radius: 4px;
width: 92%;
max-width: 600px;
resize: vertical;
background-color: #F1F1F1;
pointer-events: none;
}
.comment {
  margin-bottom: 10px;
  padding: 5px;
  border-bottom: 1px solid #ccc;
  font-size: 14px;
  color: #333;
  background-color: #fff;
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
#title, #content {
  padding: 5px;
  margin-top: 5px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
  padding: 10px;
  font-family: Arial, sans-serif;
  background-color: #F1F1F1;
  pointer-events: auto;
  overflow: auto;
  white-space: pre-line; 
  text-align: left;
}
#title {
height: 70px;
}
#content {
height: 550px;
}
.modal {
position: fixed;
top: 50%;
left: 50%;
transform: translate(-50%, -50%);
background-color: white;
padding: 1em 2em;
border-radius: 7px;
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
z-index: 1000;
border: 0.5px solid #333;
}
.modal-button {
padding: 0.1em 1em;
border-radius: 3px;
border: 0.5px solid #333; /* ボタンに枠を追加 */
cursor: pointer;
background-color: #eee;
margin: 15px 20px 0px 20px;
}
.modal-enter-active, .modal-leave-active {
transition: opacity .05s;
}
.modal-enter, .modal-leave-to {
opacity: 0;
}
.modal-mask {
position: fixed;
z-index: 999;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0,0,0,0.5);
display: flex;
justify-content: center;
align-items: center;
}

</style>