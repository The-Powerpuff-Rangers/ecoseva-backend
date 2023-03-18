import os

from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .chatbot.bot import ChatBot
from .models import UserAccount
from .serializers import (Dustbin, DustbinGroup, DustbinGroupSerializer,
                          DustbinSerializer, UserEditSerializer,
                          UserLoginSerializer, UserProfileSerializer,
                          UserRegisterSerializer)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = UserLoginSerializer(data=data)
            if serializer.is_valid():
                email = serializer.validated_data["email"]
                password = serializer.validated_data["password"]

                user = authenticate(email=email, password=password)
                if user:
                    return Response(
                        get_tokens_for_user(user), status=status.HTTP_200_OK
                    )
                else:
                    return Response(
                        {"detail": "Invalid credentials"},
                        status=status.HTTP_401_UNAUTHORIZED,
                    )
            return Response(
                {"message": "Something went wrong", "errors": serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        try:
            data = request.data
            if data["password"] != data["confirm_password"]:
                return Response(
                    {
                        "message": "Something went wrong",
                        "errors": "Password and confirm password do not match",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            serializer = UserRegisterSerializer(data=data)
            if serializer.is_valid():
                user = serializer.save()
                tokens = get_tokens_for_user(user)
                return Response(tokens, status=status.HTTP_201_CREATED)
            return Response(
                {"message": "Something went wrong", "errors": serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EditUserAPIView(APIView):
    serializer_class = UserEditSerializer

    def put(self, request):
        try:
            data = request.data
            user = request.user
            user.name = data["name"]
            user.phone = data["phone"]
            user.email = data["email"]
            user.save()
            return Response(
                {"message": "User updated successfully"}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ListUserAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserProfileSerializer

    def get(self, request):
        try:
            users = UserAccount.objects.all()
            serializer = UserProfileSerializer(users, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class CreateDustbinGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DustbinGroupSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = DustbinGroupSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Dustbin group created successfully"},
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"message": "Something went wrong", "errors": serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ListDustbinGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DustbinGroupSerializer

    def get(self, request):
        try:
            groups = DustbinGroup.objects.all()
            serializer = DustbinGroupSerializer(groups, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class CreateDustbinAPIView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = DustbinSerializer

    def post(self, request):
        try:
            data = request.data
            serializer = DustbinSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        "message": "Dustbin created successfully",
                        "data": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                {"message": "Something went wrong", "errors": serializer.errors},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EditDustbinAPIView(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = DustbinSerializer

    def put(self, request):
        try:
            data = request.data
            dustbin = Dustbin.objects.get(id=data["id"])
            dustbin.status = data["status"]
            dustbin.capacity = data["capacity"]

            dustbin.save()
            return Response(
                {"message": "Dustbin updated successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class ListDustbinsAPIView(APIView):
    serializer_class = DustbinSerializer

    def get(self, request):
        try:
            dustbins = Dustbin.objects.all()
            serializer = DustbinSerializer(dustbins, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class AddDustbinToGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = None

    def post(self, request, pk):
        try:
            data = request.data
            dustbin = Dustbin.objects.get(id=pk)
            group = DustbinGroup.objects.get(id=data["group_id"])
            dustbin.group = group
            dustbin.save()
            return Response(
                {"message": "Dustbin added successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class DeleteDustbinFromGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = None

    def delete(self, request, pk):
        try:
            dustbin = Dustbin.objects.get(id=pk)
            dustbin.group = None
            dustbin.save()
            return Response(
                {"message": "Dustbin deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class EditDustbinGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DustbinGroupSerializer

    def put(self, request):
        try:
            data = request.data
            group = DustbinGroup.objects.get(id=data["id"])
            group.name = data["name"]
            group.save()
            return Response(
                {"message": "Dustbin group updated successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class DeleteDustbinGroupAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = DustbinGroupSerializer

    def delete(self, request, pk):
        try:
            group = DustbinGroup.objects.get(id=pk)
            group.delete()
            return Response(
                {"message": "Dustbin group deleted successfully"},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


api_key = os.environ.get("API_KEY_OPENAI")
chatbot = ChatBot("gpt-3.5-turbo", api_key)


class ChatBotAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = None

    def post(self, request):
        try:
            data = request.data["message"]
            return Response(chatbot.chat(data))
        except Exception as e:
            return Response(
                {
                    "message": "Something went wrong",
                    "errors": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
