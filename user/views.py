from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, get_user_model
from .serializers import RegisterSerializer, ConfirmSerializer, LoginSerializer

User = get_user_model()


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        return Response({
            'message': 'Зарегистрирован. Код подтверждения:',
            'code': user.confirmation_code
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm(request):
    serializer = ConfirmSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        code = serializer.validated_data['code']

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

        if user.confirmation_code == code:
            user.is_active = True
            user.confirmation_code = ''
            user.save()
            return Response({'message': 'Пользователь подтверждён'}, status=status.HTTP_200_OK)

        return Response({'error': 'Неверный код'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Неверные данные'}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            return Response({'error': 'Пользователь не подтверждён'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': 'Успешный вход'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
