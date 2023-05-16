import openai
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ChatGPTView(APIView):
    def post(self, request):
        openai.api_key = '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'
        #response = openai.Completion.create(
        #    engine="text-davinci-003",
        #    prompt=request.data["diary_text"],
        #    temperature=0.5,
        #    max_tokens=100
        #)
        #return Response({"response": response.choices[0].text.strip()}, status=status.HTTP_200_OK)

        messages = [
            {"role": "system", "content": request.data["context"]},
            {"role": "user", "content": request.data["diary_text"]},
        ]
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.3,
        )

        return Response({"response": response['choices'][0]['message']['content'].strip()}, status=status.HTTP_200_OK)