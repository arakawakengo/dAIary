<template>
    <div class="upload">
        <Header/>
<!--        <head>-->
<!--          <meta charset="UTF-8">-->
<!--          <meta name="viewport" content="width=device-width, initial-scale=1.0">-->
<!--          -->
<!--        </head>-->
        <body>
            <div class="container">
              <form class="form">
                <label for="title">Title:</label>
                <input type="text" id="title" name="title">

                <label for="content">Content:</label>
                <textarea id="content" name="content"></textarea>

                <button class="post-button">Post</button>
              </form>
            </div>
        </body>



    </div>

</template>

<script>
import Header from "@/components/Header.vue";
export default {
    name: "UpLoad",
    components:{
        Header
    }
}
</script>

<style scoped>
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
  }

  .container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
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
  }

	input[type="text"] {
    height: 70px;
  }

  textarea {
    height: 550px;
  }

  .post-button {
    margin-top: 20px;
    padding: 10px 20px;
    font-size: 16px;
    border: none;
    border-radius: 4px;
    background-color: #f1f1f1;
    cursor: pointer;
  }
</style>