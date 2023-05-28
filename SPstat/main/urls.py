from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('nodereal', views.nodereal, name='nodereal'),
    path('gadgetron', views.gadgetron, name='gadgetron'),
    path('neuronet', views.neuronet, name='neuronet'),
    path('cogsworth', views.cogsworth, name='cogsworth'),
    path('thorax', views.thorax, name='thorax'),
    path('titan', views.titan, name='titan'),
    path('zenon', views.zenon, name='zenon'),
    path('volbot', views.volbot, name='volbot'),

]
