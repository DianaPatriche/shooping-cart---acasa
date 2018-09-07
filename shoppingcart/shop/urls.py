from django.urls import path,re_path
from django.conf.urls import url
from . import views


app_name='shop'


urlpatterns=[
    re_path('^$',views.product_list,name='product_list'),
    url(r'produs/',views.product_detail,name='product_detail'),
]
