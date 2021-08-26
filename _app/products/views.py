from .models import (Product)
from .serializers import (ProductSerializer)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

from .tasks import celery_perform_create_product, add

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	"""def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=False)
		celery_perform_create_product.delay(serializer.validated_data)
		#add.delay(1,2)
		return Response(serializer.validated_data, status=status.HTTP_201_CREATED)"""
	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		celery_perform_create_product.delay(serializer.validated_data)
		#add.delay(1,2)
		return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
