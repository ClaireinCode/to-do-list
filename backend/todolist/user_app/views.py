from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_404_NOT_FOUND,
    HTTP_204_NO_CONTENT,
)
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
    
from .models import User

class Sign_up(APIView):
    def post(self, request):
        request.data['username'] = request.data['email']
        my_user = User.objects.create_user(**request.data)
        token = Token.objects.create(user=my_user)

        return Response (
            {'user': my_user.email, 'token': token.key}, status=HTTP_201_CREATED
        )

class Log_in (APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        my_user = authenticate(username=email, password=password)

        if my_user:
            #get_or_create() returns a tuple: (token, created)
            #'token' is our Auth Token, 'created' is a boolean telling us if the token was created or already existed
            token, created=Token.objects.get_or_create(user=my_user)
            return Response({"token":token.key, "user": my_user.email})
        else:
            return Response("Incorrect Login", status=HTTP_404_NOT_FOUND)
        
class Info(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email})
    
class Log_out(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)