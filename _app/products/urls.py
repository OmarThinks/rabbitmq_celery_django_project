from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

from .views import (ProductViewSet)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('products', ProductViewSet)


urlpatterns = [
	path('api/', include(router.urls)),
]


#    path('api/', include((router.urls))),
