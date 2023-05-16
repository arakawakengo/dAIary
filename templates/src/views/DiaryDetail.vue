<template>
    <div class="diary_detail">
        <Header/>
        <body>
            <div>
            <!-- <div style="display: flex; justify-content: center; align-items: center; height: 100vh;"> -->
                <h1>Diary Detail</h1>
                <div class="diary-detail">
                    <h2>{{ diary.title }}</h2>
                    <p>{{ diary.content }}</p>
                    <p>{{ formatDatetime(diary.created_at) }}</p>
                </div>
                
                <h1>コメント</h1>
                <div class="comment">

                </div>

            </div>
        </body>
    </div>
</template>

<script>
import Header from "@/components/Header.vue";
import axios from 'axios';
import { toRaw } from 'vue';


export default {
    name: "DiaryDetail",
    components:{
        Header
    },
    data() {
        return {
            diary_id: "",
            diary: []
        };
    },
    async created() {
    try {
        const diary_id = this.$route.params.diary_id
        const token = localStorage.getItem("access");
        const response = await axios.get(`http://localhost:8000/api/diaries/${diary_id}`, {
            headers: {
                'Authorization': `Bearer ${token}`,
            },
        });
        const rawRes = toRaw(response.data);
        const jsonString = JSON.stringify(rawRes);
        this.diary = JSON.parse(jsonString);
    } catch (error) {
        console.error("Failed to fetch diaries.");
        console.error(error);
    }
  },
  methods: {
  formatDatetime(datetime) {
    const date = new Date(datetime);
    const year = date.getFullYear();
    const month = ("0" + (date.getMonth() + 1)).slice(-2);
    const day = ("0" + date.getDate()).slice(-2);
    const hour = ("0" + date.getHours()).slice(-2);
    const minute = ("0" + date.getMinutes()).slice(-2);
    return `${year}-${month}-${day} ${hour}:${minute}`;
  },
},
}
</script>


<style scoped>
    /* ページ全体のレイアウト */
    body {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    
    /* h2要素全般（Diary Detailとコメントの見出し） */
    h1 {
        color: #333;
        font-size: 28px;
        margin: 20px 0;
    }

    /* 日記詳細スタイル */
    .diary-detail {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 20px;
        background-color: #f0f0f0;
        border-radius: 5px;
        width: 80%;
        min-height: 200px;
        min-width: 300px;
        margin-bottom: 20px;
    }
    .diary-detail h2 {
        color: #444;
        font-size: 24px;
        margin-bottom: 10px;
    }
    .diary-detail p {
        color: #666;
        font-size: 16px;
        line-height: 1.6;
    }

    /* コメントセクションのスタイル */
    .comment {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        padding: 20px;
        background-color: #f0f0f0;
        border-radius: 5px;
        width: 80%;
        min-width: 300px;
    }
</style>
