<template>
    <div class="diary_detail">
        <Header/>
        <body>
            <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
                <form class="form">
                    <div class="input-group">
                        <label class="past-diary-label" for="past-diary">自分が書いた過去の日記
                            <span class="date">2023-04-25</span>
                        </label>
                        <textarea id="past-diary" class="past-diary-input" readonly></textarea>
                    </div>
                    <div class="input-group">
                        <label class="comment-label" for="comment">コメント：</label>
                        <textarea id="comment" class="comment-input"></textarea>
                    </div>
                </form>
            </div>
        </body>
    </div>
</template>
<script>
import Header from "@/components/Header.vue";
export default {
    name: "DiaryDetail",
    components:{
        Header
    }
}
</script>


<style scoped>
        /* 横着的菜单栏样式 */
        .menu {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #F1F1F1;
            height: 50px;
            padding: 0 20px;
        }
        .menu-item {
            font-size: 18px;
            padding: 10px 20px;
            cursor: pointer;
        }
        /* 输入框样式 */
        .form {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 50px;
        }
        label {
            font-size: 18px;
            margin-top: 10px;
        }
        .input-group {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin-top: 20px;
            width: 1000px;
        }
        .comment-input {
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 10px;
            font-size: 16px;
            resize: none;
            min-height: 200px;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
            margin-bottom: 20px;
        }
        .past-diary-input {
            width: 100%;
            border: 1px solid #ccc;
            border-radius: 4px;
            padding: 10px;
            font-size: 16px;
            resize: none;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
            margin-bottom: 20px;
        }
        .past-diary-label {
            position: relative;
            font-size: 18px;
            margin-top: 10px;
            width: 1000px;
        }
        .date {
            position: absolute;
            top: -25px;
            right: 0;
            font-size: 14px;
            color: #999;
        }
    </style>