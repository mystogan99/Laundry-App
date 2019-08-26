from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from orders import views 
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

from orders import views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.client, name='index'),
    # url(r'^$', my_order.index, name='home'),
    # url(r'^client$', my_order.client, name='client'),
    url(r'^succesfull$', views.succesfull, name='succesfull'),
    url(r'^HolyGrail$', views.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', views.show, name='show'),
    url(r'^order/new/$', views.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', views.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', views.destroy, name='delete'),
    url(r'^products$', views.index_product, name='home_product'),
    url(r'^product/new/$', views.new_product, name='new_product'),
    url(r'^product/delete/(?P<product_id>\d+)/$', views.destroy_product, name='delete_product'),
    url(r'^users/login/$', auth.login, {'template_name': 'login2.html'}, name='login'),
    url(r'^users/logout/$', auth.logout, {'next_page': 'login'}, name='logout'),
    url(r'^users/change_password/$', login_required(auth.password_change), {'post_change_redirect' : '/HolyGrail','template_name': 'change_password.html'}, name='change_password'),
]
