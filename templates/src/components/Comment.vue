<template>
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
        <select class="dropdown">
          <option value="Option 1">Option 1</option>
          <option value="Option 2">Option 2</option>
          <option value="Option 3">Option 3</option>
        </select>
        <select class="dropdown">
          <option value="Option 4">Option 4</option>
          <option value="Option 5">Option 5</option>
          <option value="Option 6">Option 6</option>
        </select>
    </div>
    <button class="button additional-button" style="margin-bottom: 30px;">  <!-- Increased margin -->
        Additional Button
    </button>
    <textarea class="comment" rows="5" readonly></textarea>
    </div>
  </div>
</body>
</template>

<script setup>
export default {
    name: "Comment",
}
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