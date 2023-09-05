from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import User, Post, Comment
from .serializers import UserSerializer, UserRegistrationSerializer, UserLoginSerializer, PostSerializer, CommentSerializer

class Socialize(APIView):
    permission_classes = [IsAuthenticated]

    def get_user_detail(self, user_id):
        user = User.objects.get(id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create_post(self, data):
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def get_post_detail(self, post_id):
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create_comment(self, data):
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def user_register(self, data):
        serializer = UserRegistrationSerializer(data=data)
        user = serializer.save()
        return Response(serializer.data)

    def user_login(self, data):
        serializer = UserLoginSerializer(data=data)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Login failed"}, status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        action = request.data.get("action")

        if action == "user_detail":
            user_id = request.data.get("user_id")
            return self.get_user_detail(user_id)

        elif action == "create_post":
            return self.create_post(request.data)

        elif action == "post_detail":
            post_id = request.data.get("post_id")
            return self.get_post_detail(post_id)

        elif action == "create_comment":
            return self.create_comment(request.data)

        elif action == "user_register":
            return self.user_register(request.data)

        elif action == "user_login":
            return self.user_login(request.data)

