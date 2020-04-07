from django.contrib.auth.models import User 
from rest_framework import serializers 
from rest_framework_jwt.settings import api_settings
from .models import Classification, Service, Item, OrderItem, UserOrder


class StringSerializer(serializers.StringRelatedField):
	def to_internal_value(self, value):
		return value


class UserCreateSerializer(serializers.ModelSerializer):
	password= serializers.CharField(write_only=True)
	class Meta:
		model= User
		fields= ['username', 'email', 'password']

	def create(self, validated_data):
		username= validated_data['username']
		email= validated_data['email']
		password= validated_data['password']
		new_user= User(username=username, email=email)
		new_user.set_password(password)
		new_user.save()
		return validated_data

class UserLoginSerializer(serializers.Serializer):
	username=serializers.CharField()
	password= serializers.CharField(write_only=True)
	token = serializers.CharField(allow_blank=True, read_only=True)

	def validate(self, data):
		my_username= data.get('username')
		my_password= data.get('password')

		try:
			user_obj= User.objects.get(username=my_username)

		except:
			raise serializers.ValidationError("This username does not exist")

		if not user_obj.check_password(my_password):
			raise serializers.ValidationError("Incorrect username/password combination")

		jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
		jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

		payload = jwt_payload_handler(user_obj)
		token = jwt_encode_handler(payload)

		data["token"] = token
		return data

class ClassificationSerializer(serializers.ModelSerializer):
	class Meta:
		model: Classification
		fields= ['id', 'name', 'image']

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model: Service
		fields= '__all__'

class ItemSerializer(serializers.ModelSerializer):
	#to obtain the value from the model's ForeignKey fields instead of id
	iron= serializers.SlugRelatedField (slug_field='price', queryset=Service.objects.all())
	dry_clean= serializers.SlugRelatedField (slug_field='price', queryset=Service.objects.all())
	laundry= serializers.SlugRelatedField (slug_field='price', queryset=Service.objects.all())
	classification= serializers.SlugRelatedField (slug_field='name', queryset=Classification.objects.all())
	class Meta:
		model= Item
		fields= ['id', 'classification', 'item_name', 'iron', 'dry_clean', 'laundry']
		
class OrderItemSerializer(serializers.ModelSerializer):
	# we are setting the item to have only the string value of model Item(item_name)
	item= StringSerializer()
	item_id= serializers.SerializerMethodField()

	class Meta:
		model= OrderItem
		fields= ['id', 'item', 'quantity', 'item_price', 'service', 'item_id']
	def get_item_id(self, obj):
		return obj.item.id

class UserOrderSerializer(serializers.ModelSerializer):
	# we have to serialize the order items that belong to the order
	order_items= serializers.SerializerMethodField()
	class Meta:
		model= UserOrder
		fields= ['order_items']

	def get_order_items(self, obj):
		return OrderItemSerializer(obj.items.all(), many=True).data







