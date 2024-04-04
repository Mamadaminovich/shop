from django.urls import include, path
from rest_framework import routers
from .views import *

urlpatterns = [    
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('rpage/', regular_page, name='regular_page'),
    path('shop/', shop, name='shop'),
    path('sblog/', single_blog, name='single_blog'),
    path('spdetails/', single_product_details, name='single_product_details'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]