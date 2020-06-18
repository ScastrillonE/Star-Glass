from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServiceList.as_view(), name='services'),
    path('service/detail/<int:pk>/', serviceDetail, name='service_detail')
]