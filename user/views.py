from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import permissions, serializers
from rest_framework.views import APIView
from user.models import advisior_info
from user.serializers import advisior_info_Serializer, UserSerializer
from rest_framework.authtoken.models import Token
# Used for basic Token authentication
# from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class Homepage(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        print("Username:", request.user)
        advisior_info_obj = advisior_info.objects.all()
        serializers = advisior_info_Serializer(advisior_info_obj, many=True)
        return Response({'status':200, 'message':serializers.data})


class RegisterUser(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserSerializer(data= request.data)

        if not serializer.is_valid():
            return Response({'status': 403, 'errors':serializer.errors, 'message' : 'Ceredentials were not provided properly please try again!'})
        serializer.save()
        user = User.objects.get(username = serializer.data['username'])
        # token_obj , _ = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)
        return Response({'status':200, 
                        'payload': serializer.data, 
                        'refresh': str(refresh),
                        'access': str(refresh.access_token), 
                        'message': 'User has been generated'
                        })    