from django.forms import ModelForm
from django import forms
from .models import Order, Product


class OrderForm(ModelForm):
    OPTIONS = (
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
        ('Ready', 'Ready'),
        ('Send', 'Send'),
        ('Delivered', 'Delivered'),
        ('Returned', 'Returned'),
        ('Cancelled', 'Cancelled')
    )
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect, initial='Send')
    payment_option = forms.ChoiceField(required=False, choices=OPTIONS, initial= 'Postpay')
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active='1'), empty_label='')
    delivery_date = forms.DateField(required=True)
    quantity = forms.IntegerField(required=False)

    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','quantity','order_status']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name','product_details','price']

# =========modal form======= #
class userform(ModelForm):
    OPTIONS = (
        ('Postpay','Postpay'),
        ('Prepay (Full)','Prepay (Full)'),
        ('Prepay (Half)', 'Prepay (Half)')
    )
    OPTIONS2 = (
        ('Confirm', 'Confirm'),
    )

    payment_option = forms.ChoiceField(required=False, choices=OPTIONS, initial= 'Postpay')
    product_id = forms.ModelChoiceField(queryset=Product.objects.filter(active='1'), empty_label='')
    delivery_date = forms.DateField(required=True)
    quantity = forms.IntegerField(required=False, initial=1)
    order_status = forms.TypedChoiceField(required=False, choices=OPTIONS2, widget=forms.RadioSelect, initial='Confirm')
    class Meta:
        model = Order
        fields = ['name','phone','address','delivery_date','product_id','payment_option','quantity','order_status']
        # exclude = ('order_status',)
# =========modal form======= #