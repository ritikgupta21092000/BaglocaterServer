from django.urls import path
from . import views

urlpatterns = [
    path('decode', views.decode, name='decode'),
    path('authenticate', views.authenticate, name='authenticate'),
    path('addLostAndFound', views.addLostAndFound, name='addLostAndFound'),
    path('retrievebag', views.retrievebag, name='retrievebag'),
    path('searchBags', views.searchBags, name='searchBags'),
    path('verifydetails', views.verifydetails, name='verifydetails')
]
