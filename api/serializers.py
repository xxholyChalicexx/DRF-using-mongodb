from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User, Student


class UserSerializer(serializers.ModelSerializer):
	
	email = serializers.EmailField(
			required = True,
			validators=[UniqueValidator(queryset=User.objects.all())],
		)
	password = serializers.CharField(min_length=8, write_only=True)
	confirm_password = serializers.CharField(min_length=8, write_only=True)
	phone_number = serializers.CharField(min_length=10, validators = [UniqueValidator(queryset=User.objects.all())])
	first_name = serializers.CharField(min_length=3)
	last_name = serializers.CharField(min_length=3)

	def create(self, validated_data):
		user = User.objects.create_user(email =  validated_data['email'], password = validated_data['password'], phone_number = validated_data['phone_number'],first_name=validated_data['first_name'], last_name=validated_data['last_name'])

		return user

	def validate(self, data):
		if data.get('password') != data.get('confirm_password'):
			raise serializers.ValidationError({"password":"Those passwords don't match."})
		if data.get('first_name') == "":
			raise serializers.ValidationError({"first_name":"First name field empty"})
		return data
	class Meta:
		model = User
		fields = ('id', 'email', 'password','phone_number','first_name','last_name', 'confirm_password')



class StudentSerializer(serializers.ModelSerializer):
	first_name = serializers.CharField(min_length=2)
	last_name = serializers.CharField(min_length=2)
	standard = serializers.CharField(min_length=1)
	date_of_birth = serializers.CharField(min_length=1)
	

	def create(self, validated_data):
		student = Student.objects.create(user = validated_data['user'],first_name=validated_data['first_name'],last_name=validated_data['last_name'], standard=validated_data['standard'],board = validated_data['board'], date_of_birth = validated_data['date_of_birth'])
		return student
	
	class Meta:
		fields = (
			'id',
			'first_name',
			'last_name',
			'standard',
			'board',
			'date_of_birth',
		)
		model = Student


# 		{
# "username":"aniket",
# "email":"test@test.com",
# "password":"test1234",
# "extra":{
# "date_of_birth":"1992-09-06"
# "contact_number":"7411833378"
# }
# }