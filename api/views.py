from rest_framework.authtoken.models import Token
from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from  django.contrib.auth.models import User

from api.serializers import UserSerializer, StudentSerializer
from .models import Student

# Create your views here
class StudentList(APIView):
	
	def get(self, request):
		snippet = Student.objects.filter(user=request.user)
		serializer = StudentSerializer(snippet, many=True)
		return Response(serializer.data)
	
	def post(self,request):
		print(self.request.user)
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			print(self.request.user)
			serializer.save(user=self.request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response({'status':'error'})

class StudentDetail(APIView):

	def get(self, request, pk):
		print(pk)
		snippet = Student.objects.filter(id=pk)
		serializer = StudentSerializer(snippet, many=True)
		return Response(serializer.data)



class UserCreate(APIView):
	"""
	Creates the user
	"""
	def post(self, request, format='json'):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				token = Token.objects.create(user=user)
				json = serializer.data
				json['token'] = token.key
				return Response(json, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

