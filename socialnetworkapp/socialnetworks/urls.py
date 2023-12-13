

from django.urls import path, include
from rest_framework import routers
from socialnetworks import views


router = routers.DefaultRouter()
router.register('Posts', views.PostViewSet, basename='posts')
router.register('Auctions', views.AuctionViewSet, basename='auctions')

urlpatterns = [
    path('', include(router.urls))
]
