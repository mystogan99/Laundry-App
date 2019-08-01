from django.shortcuts import render, redirect
from .models import Order, Product
from django.core.mail import send_mail
from django.conf import settings
from .forms import OrderForm, ProductForm, userform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import requests
import json

URL = 'https://www.160by2.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo, 
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)


def succesfull(request):
     return render(request, 'succesfull.html')




def client(request):
    if request.POST:
        form = userform(request.POST)
        if form.is_valid():
            subject = "Order from laundry city"
            from_email = settings.EMAIL_HOST_USER
            to_email = form.cleaned_data['email']
            message = "Your order has been placed succesfully. Your valet with reach you soon."
            phone = form.cleaned_data['phone']
            response = sendPostRequest(URL, 'RJGUGSAI8ER4DL8SMWICU2TJ4RNGT1Y2', 'PAFW2F2SHJSX811P', 'stage', phone, '7014831301', 'Hey, your  order has been placed.' )
            try:
                send_mail(subject, message, from_email, [to_email], fail_silently = False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            if form.save():
                return redirect('/succesfull', messages.success(request, 'Order was successfully created.', 'alert-success'))
                
            else:
                return redirect('/succesfull', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/succesfull', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = userform()
        return render(request, 'client.html', {'form':form})




@login_required
def index(request):
    orders = Order.objects.all()
    return render(request, 'index.html', {'orders': orders})

@login_required
def show(request, order_id):
    order = Order.objects.filter(id=order_id)
    return render(request, 'show.html', {'order': order})

@login_required
def new(request):
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/HolyGrail', messages.success(request, 'Order was successfully created.', 'alert-success'))
            else:
                return redirect('/HolyGrail', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/HolyGrail', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm()
        return render(request, 'new.html', {'form':form})

@login_required
def edit(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.POST:
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            if form.save():
                return redirect('/HolyGrail', messages.success(request, 'Order was successfully updated.', 'alert-success'))
            else:
                return redirect('/HolyGrail', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/HolyGrail', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        form = OrderForm(instance=order)
        return render(request, 'edit.html', {'form':form})

@login_required
def destroy(request, order_id):
    order = Order.objects.get(id=order_id)
    order.delete()
    return redirect('/HolyGrail', messages.success(request, 'Order was successfully deleted.', 'alert-success'))



#Product

@login_required
def index_product(request):
    products = Product.objects.filter(active='1')
    return render(request, 'index_product.html', {'products': products})    

@login_required
def new_product(request):
    if request.POST:
        form = ProductForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('/products', messages.success(request, 'Product was successfully created.', 'alert-success'))
            else:
                return redirect('/products', messages.error(request, 'Data is not saved', 'alert-danger'))
        else:
            return redirect('/products', messages.error(request, 'Form is not valid', 'alert-danger'))
    else:
        product_form = ProductForm()
        return render(request, 'new_product.html', {'product_form':product_form})    

@login_required
def destroy_product(request, product_id):
    #order = Order.objects.filter(product_id=product_id).count()

    #if order > 0:
    #     return redirect('/products', messages.success(request, 'Cannot delete product while its order exists.', 'alert-danger'))    
    #else:
    #    product = Product.objects.get(id=product_id)
    #    product.delete()
    #    return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))      

    if Product.objects.filter(id=product_id).update(active='0'):
        return redirect('/products', messages.success(request, 'Product was successfully deleted.', 'alert-success'))  
    else:
        return redirect('/products', messages.danger(request, 'Cannot delete product while its order exists.', 'alert-danger'))  