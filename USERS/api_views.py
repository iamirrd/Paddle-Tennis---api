from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import logout
from .serializers import RegisterSerializer, ChangePasswordSerializer, UserSerializer


class RegisterView(APIView):
    """
    ثبت‌نام کاربر جدید
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "ثبت‌نام با موفقیت انجام شد"},
            status=status.HTTP_201_CREATED
        )


class LogoutView(APIView):
    """
    خروج از حساب کاربری
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response(
            {"message": "با موفقیت خارج شدید"},
            status=status.HTTP_200_OK
        )


class ProfileView(APIView):
    """
    نمایش اطلاعات پروفایل کاربر
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    """
    تغییر رمز عبور کاربر
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user

        if not user.check_password(serializer.validated_data['old_password']):
            return Response(
                {"old_password": "رمز فعلی اشتباه است"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.set_password(serializer.validated_data['new_password'])
        user.save()

        return Response(
            {"message": "رمز عبور با موفقیت تغییر کرد"},
            status=status.HTTP_200_OK
        )