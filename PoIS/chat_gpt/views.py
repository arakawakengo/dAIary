import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

API_KEY = os.environ.get("API_KEY")

class ChatGPTView(APIView):
    def post(self, request):
        openai.api_key = API_KEY

        messages = [
            {"role": "system", "content": request.data["context"]},
            {"role": "user", "content": request.data["diary_text"]},
        ]
        
        response = openai.ChatCompletion.create(\
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,
        )

        return Response({"response": response['choices'][0]['message']['content'].strip()}, status=status.HTTP_200_OK)