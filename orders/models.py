from django.db import models

# Create your models here.
class Product(models.Model):
	product_name = models.CharField(max_length=200)
	product_details = models.TextField()
	price = models.IntegerField()
	active = models.IntegerField(default='1')

	def __str__(self):
		return '%s (%s tk)' % (self.product_name, self.price)

class Order (models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100,  default="")
    address = models.TextField()
    delivery_date = models.DateField(blank=True)
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    quantity = models.IntegerField()
