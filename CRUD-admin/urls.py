from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from orders import views as my_order
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')), 
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', admin.site.urls),
    url(r'^$', my_order.index, name='home'),
    url(r'^orders$', my_order.index, name='home'),
    url(r'^order/(?P<order_id>\d+)/$', my_order.show, name='show'),
    url(r'^order/new/$', my_order.new, name='new'),
    url(r'^order/edit/(?P<order_id>\d+)/$', my_order.edit, name='edit'),
    url(r'^order/delete/(?P<order_id>\d+)/$', my_order.destroy, name='delete'),
    url(r'^products$', my_order.index_product, name='home_product'),
    url(r'^product/new/$', my_order.new_product, name='new_product'),
    url(r'^product/delete/(?P<product_id>\d+)/$', my_order.destroy_product, name='delete_product'),
    url(r'^users/login/$', auth.login, {'template_name': 'login.html'}, name='login'),
    url(r'^users/logout/$', auth.logout, {'next_page': '/'}, name='logout'),
    url(r'^users/change_password/$', login_required(auth.password_change), {'post_change_redirect' : '/','template_name': 'change_password.html'}, name='change_password'),
]
