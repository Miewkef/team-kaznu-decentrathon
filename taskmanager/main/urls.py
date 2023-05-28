from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about, name='about'),
    path('prices', views.price, name='price'),
    path('set', views.set, name='set'),
]
