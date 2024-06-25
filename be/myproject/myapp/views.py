from django.contrib.auth.hashers import make_password
from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User as UserProfile, User, UserPreferencesLink
from .models import Project
from .serializers import ProjectSerializer, UserSerializer, UserPreferencesLinkSerializer


# from .utils import generate_auth_token 


def generate_auth_token(user):
    token, created = Token.objects.get_or_create(user=user)
    return token.key


# def mock_authenticate(email, password):
#     test_email = 'test@example.com'
#     test_password = 'testpassword'

#     if email == test_email and password == test_password:

#         return {
#             'id': 1,
#             'username': 'testuser',
#             'email': test_email,
#         }
#     return None

# @csrf_exempt
# def student_login(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             email = data.get('email')
#             password = data.get('password')
#             print(f"email is {email}")
#             print(f"password is {password}")
#             if not email or not password:
#                 return JsonResponse({'error': 'Email and password are required.'}, status=400)

#             user = mock_authenticate(email, password)
#             print(user)
#             if user is not None:

#                 auth_token = 'mocktoken12345'
#                 response_data = {
#                     'user_profile': {
#                         'id': user['id'],
#                         'name': user['username'],
#                         'email': user['email'],
#                     },
#                     'auth_token': auth_token
#                 }
#                 return JsonResponse(response_data, status=200)
#             else:
#                 return JsonResponse({'error': 'Invalid email or password.'}, status=401)

#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
#     else:
#         return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)


############################################################################################
#                                    Student Sign up                                       #
############################################################################################
@csrf_exempt
def student_signup(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            first_name = data.get('FirstName')
            last_name = data.get('LastName')
            email = data.get('EmailAddress')
            password = data.get('Passwd')
            username = email  # 使用电子邮件作为用户名

            if not first_name or not last_name or not email or not password:
                return JsonResponse({'error': 'FirstName, LastName, EmailAddress, and Passwd are required.'},
                                    status=400)

            if User.objects.filter(username=username).exists():
                return JsonResponse({'error': 'Username already exists.'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'error': 'Email already exists.'}, status=400)

            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name,
                                            last_name=last_name)
            token = Token.objects.create(user=user)

            return JsonResponse({
                'token': token.key,
                'user': {
                    'UserID': user.pk,
                    'FirstName': user.first_name,
                    'LastName': user.last_name,
                    'EmailAddress': user.email,
                    'Username': user.username
                }
            }, status=status.HTTP_201_CREATED)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)


############################################################################################
#                                    Student Login                                         #
############################################################################################
@csrf_exempt
def student_login(request):
    if request.method == 'POST':
        try:
            # User Authentication
            data = json.loads(request.body)
            email = data.get('email')
            password = data.get('password')
            if not email or not password:
                return JsonResponse({'error': 'Email and password are required.'}, status=400)
            user = authenticate(request, username=email, password=password)

            if user is not None:
                # Assuming the UserProfile model has a foreign key relationship with the User model
                user_profile = UserProfile.objects.get(user=user)
                auth_token = generate_auth_token(user)
                response_data = {
                    'user_profile': {
                        'UserID': user_profile.id,
                        'FirstName': user_profile.Firstname,
                        'LastName': user_profile.LastName,
                        'EmailAddress': user_profile.user.email,
                    },
                    'auth_token': auth_token
                }
                return JsonResponse(response_data, status=200)
            else:
                if not User.objects.filter(email=email).exists():
                    return JsonResponse({'error': 'E-mail not found.'}, status=404)
                else:
                    return JsonResponse({'error': 'Incorrect password. Please try again.'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format.'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)


############################################################################################
#                                    Project Creation                                      #
############################################################################################
@csrf_exempt
def project_creation(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        # print(data)

    # User Authentication
    auth_token = data.get('auth_token')
    try:
        token = Token.objects.get(key=auth_token)
        user = token.user
    except Token.DoesNotExist:
        return JsonResponse({'error': 'Authentication failed'}, status=401)

    serializer = ProjectSerializer(data=data)
    if serializer.is_valid():
        serializer.save(created_by=user)
        return JsonResponse({'message': 'Project created successfully!', 'project': serializer.data}, status=201)
    return JsonResponse(serializer.errors, status=400)


############################################################################################
#                                    Project Updating                                      #
############################################################################################
@csrf_exempt
def project_update(request, id):
    try:
        project = Project.objects.get(pk=id)
    except:
        return JsonResponse({'error': 'Project not found'}, status=404)

    if request.method == 'Put':
        data = JSONParser().parse(request)

    # User Authentication
    auth_token = data.get('auth_token')
    try:
        token = Token.objects.get(key=auth_token)
        user = token.user
    except Token.DoesNotExist:
        return JsonResponse({'error': 'Authentication failed'}, status=401)

    serializer = ProjectSerializer(data=data)
    if serializer.is_vaild():
        serializer.save(created_by=user)
        return JsonResponse({'message': 'Project updated successfully!', 'project': serializer.data}, status=200)
    return JsonResponse(serializer.error, staus=400)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            if 'Passwd' in serializer.validated_data:
                serializer.validated_data['Passwd'] = make_password(serializer.validated_data['Passwd'])
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_preferences(request):
    user = request.user

    if request.method == 'GET':
        preferences = UserPreferencesLink.objects.filter(UserID=user)
        serializer = UserPreferencesLinkSerializer(preferences, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['UserID'] = user.UserID
        serializer = UserPreferencesLinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def user_preference_detail(request, pk):
    user = request.user

    try:
        preference = UserPreferencesLink.objects.get(pk=pk, UserID=user)
    except UserPreferencesLink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserPreferencesLinkSerializer(preference, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        preference.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
