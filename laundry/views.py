from .serializers import UserCreateSerializer, UserLoginSerializer, ClassificationSerializer, ServiceSerializer, ItemSerializer, OrderItemSerializer, UserOrderSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import Classification, Service, Item, OrderItem, UserOrder
from rest_framework.response import Response
import json 
from django.core.exceptions import ObjectDoesNotExist
from decimal import *

class UserCreateAPIView(CreateAPIView):
	serializer_class= UserCreateSerializer

class UserLoginAPIView(APIView):
	serializer_class= UserLoginSerializer

	def post(self, request):
		my_data= request.data
		serializer= UserLoginSerializer(data=my_data)
		if serializer.is_valid(raise_exception=True):
			valid_data= serializer.data
			return Response(valid_data, status=HTTP_200_OK)
		return Response(serializer.errors, HTTP_400_BAD_REQUEST)

class ClassificationAPIView(ListAPIView):
	queryset= Classification.objects.all()
	serializer_class= ClassificationSerializer

class ServiceAPIView(ListAPIView):
	queryset= Service.objects.all()
	serializer_class= ServiceSerializer

class ServiceCreateView(CreateAPIView):
	# permission_class=[IsAdminUser]
	serializer_class= ServiceSerializer

class ItemListView(ListAPIView):
	# permission_class=[AllowAny]
	queryset= Item.objects.all()
	serializer_class= ItemSerializer

class ItemCreatView(CreateAPIView):
	# permission_class=[IsAdminUser]
	serializer_class= ItemSerializer	

class AddToCartView(APIView):
	# permission_class=[IsAuthenticated]

	def post(self, request):
		print('data',request.data)
		print('user', request.user)
		data=request.data
		quantity=data['quantity']
		print('quantity', quantity)
		item_id=data['id']
		print('item_id', item_id)
		total=data['total']
		print('total', total)
		service=data['service']
		print('service', service)


		item= Item.objects.get(id=item_id)
		order_item, created = OrderItem.objects.get_or_create(user=request.user, item=item, service=service, status=False)
		print('order_item', order_item)
		order_qs= UserOrder.objects.filter(user=request.user, status=False)
		# There is an order already
		if order_qs.exists():
			order=order_qs[0]
			my_order=order.items.filter(item=item, service=service)
			# This item(with this service) exists
			if my_order.exists():
				print('found')
				order_item.quantity +=quantity
				order_item.item_price +=Decimal(total)
				# order_item.service= service
				order_item.save()
				
				return Response({'message':"success"}, status=HTTP_200_OK)
			#First time adding this item(with this service)
			else:
				print('here')
				order_item.quantity=quantity
				order_item.item_price=total
				# order_item.service= service
				order_item.save()
				order.items.add(order_item)
				
				return Response({'message':"success"}, status=HTTP_200_OK)
		#No orders made yet		
		else:
			#add time for the added piece
			print('there')
			order=UserOrder.objects.create(user=request.user)
			order_item.quantity=quantity
			order_item.item_price=total
			# order_item.service= service
			order_item.save()
			order.items.add(order_item)
			
			return Response({'message':"success"}, status=HTTP_200_OK)


	def get(self, request):
		print('requestedUser', request.user)
		try:
			order= UserOrder.objects.filter(user=request.user)
			serializer= UserOrderSerializer(order, many=True)
			return Response(serializer.data)
		except ObjectDoesNotExist:
			return Response({'message': "You hane not submitted any order"}, status=HTTP_400_BAD_REQUEST)

class OrderSummaryView(APIView):
		def get(self, request):
			print('requestedUser', request.user)
			try:
				order= UserOrder.objects.filter(user=request.user, status=True)
				serializer= UserOrderSerializer(order, many=True)
				return Response(serializer.data)
			except ObjectDoesNotExist:
				return Response({'message': "You hane not submitted any order"}, status=HTTP_400_BAD_REQUEST)

class CheckoutView(APIView):
	def post(self, request):
			order = UserOrder.objects.filter(user=request.user, status=False)
			order.status= True
			print('this order',order.status)
			# order.save()
			return Response({'msg': 'status modified'})

class RemoveFromCartView(APIView):
	def post(self, request):
		print('data',request.data)
		print('user', request.user)
		data=request.data
		quantity=data['quantity']
		print('quantity', quantity)
		item_id=data['item_id']
		print('item_id', item_id)
		service=data['service']
		print('service', service)

		item= Item.objects.get(id=item_id)
		order_qs= UserOrder.objects.filter(user=request.user, status=False)
		if order_qs.exists():
			print('here')
			order= order_qs[0]
			my_order=order.items.filter(item=item, service=service)
			if my_order.exists():
				print('now here')
				order_item = OrderItem.objects.filter(user=request.user, item=item, service=service, status=False)[0]
				order.items.remove(order_item)
				return Response({'message':"Item is removed"}, status=HTTP_200_OK)
			else:
				return Response({'message': "This item doesn't exist in your cart"}, status=HTTP_400_BAD_REQUEST)
		else:
			return Response({'message': "There is no active order!"}, status=HTTP_400_BAD_REQUEST)


class ItemUpdateView(RetrieveUpdateAPIView):
	permission_class=[IsAdminUser]
	queryset= Item.objects.all()
	serializer_class= ItemSerializer
	lookup_field= 'id'
	lookup_url_kwarg= 'item_id'



