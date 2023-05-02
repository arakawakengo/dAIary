<template>
<!--<!DOCTYPE html>-->
<!--<html>-->
<head>
	<title>Randomiary</title>

</head>
<body>
	<div class="menu">
		<h1>Randomiary</h1>
		<div>
			<span class="menu-item">プロファイル</span>
			<span class="menu-item">日記作成</span>
		</div>
	</div>

	<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
		<form class="form">
			<label for="title">日記タイトル:</label>
			<input type="text" id="title" name="title">

			<label for="content">日記内容:</label>
			<textarea id="content" name="content"></textarea>

			<input type="submit" value="日記投稿">
		</form>
	</div>
</body>
<!--</html>-->


</template>

<script>
export default {
    name: "UpLoad"
}
</script>

<style scoped>
.menu {
			display: flex;
			justify-content: space-between;
			align-items: center;
			background-color: #f1f1f1;
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

		input[type="text"], textarea {
			padding: 5px;
			margin-top: 5px;
			font-size: 16px;
			border: 1px solid #ccc;
			border-radius: 4px;
			width: 1000px;
			resize: none;
			box-sizing: border-box;
			padding: 10px;
			font-family: Arial, sans-serif;
		}

		input[type="text"] {
			height: 200px;
		}

		textarea {
			height: 400px;
		}

		input[type="submit"] {
			background-color: #4CAF50;
			color: white;
			padding: 10px 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-size: 18px;
			margin-top: 20px;
		}

		input[type="submit"]:hover {
			background-color: #45a049;
		}
</style>