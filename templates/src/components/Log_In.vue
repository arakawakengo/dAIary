<template>
<head>
	<title>dAIary</title>
</head>
<body>
	<h1 style="text-align: left;">dAIary</h1>

	<div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
		<form>
			<label for="username">Username:</label>
			<input type="text" id="username" name="username">

			<label for="password">Password:</label>
			<input type="password" id="password" name="password">

			<input type="submit" value="Log_In">
			<button id="register-btn">Sign Up</button>
		</form>
	</div>
</body>

</template>

<script>
export default {
    name: "Log_In"
}
</script>

<style scoped>
	form {
			display: flex;
			flex-direction: column;
			align-items: center;
			margin-top: 50px;
		}

		label {
			font-size: 18px;
			margin-top: 10px;
		}

		input[type="text"], input[type="password"] {
			padding: 5px;
			margin-top: 5px;
			font-size: 16px;
			border: 1px solid #ccc;
			border-radius: 4px;
			width: 250px;
			height: 30px;
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

		#register-btn {
			background-color: #008CBA;
			color: white;
			padding: 10px 20px;
			border: none;
			border-radius: 4px;
			cursor: pointer;
			font-size: 18px;
			margin-top: 20px;
		}

		#register-btn:hover {
			background-color: #007a99;
		}
</style>