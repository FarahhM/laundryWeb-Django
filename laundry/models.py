from django.db import models
from django.contrib.auth.models import User
# from django.db.models import Sum

class Classification(models.Model):
	name= models.CharField(max_length=120)
	image= models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

class Service(models.Model):
	service= models.CharField(max_length=100)
	description= models.TextField(max_length=500)
	price= models.DecimalField(max_digits=5, decimal_places=3, null=True)

	def __str__(self):
		return self.service


class Item(models.Model):
	classification= models.ForeignKey(Classification, on_delete=models.CASCADE)
	item_name= models.CharField(max_length=120)
	iron= models.ForeignKey(Service, on_delete=models.CASCADE, null=True,  related_name='iron+', default=0 )
	dry_clean= models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='dry+', default=0)
	laundry= models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='laundry+', default=0)
	

	def __str__(self):
		return self.item_name

class OrderItem(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	status= models.BooleanField(default=False)
	item= models.ForeignKey(Item, on_delete=models.CASCADE)
	quantity= models.IntegerField(default=1)
	item_price= models.DecimalField(max_digits=5, decimal_places=3, null=True)
	service= models.CharField(max_length=30, null=True, blank=True)
	# total= models.IntegerField(max_length=30, null=True, blank=True)
	def __str__(self):
		return self.item.item_name
	# def total_order(self):
	# 	total=0
	# 	price=0
	# 	i=self.item
	# 	#price=sum([x.iron.price, x.dry_clean.price, x.laundry.price for x in self.item])
	# 	price=sum(i.iron.price, i.dry_clean.price, i.laundry.price)
	# 	total+=(self.quantity*price)
	# 	return total
		

class UserOrder(models.Model):
	user= models.ForeignKey(User, on_delete=models.CASCADE)
	items= models.ManyToManyField(OrderItem)
	status= models.BooleanField(default=False)
	date_time= models.DateTimeField(auto_now_add=True, null=True, blank=True)

	# def __str__(self):
	# 	return self.items


