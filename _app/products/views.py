from .models import (Product)
from .serializers import (ProductSerializer)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
import pprint
pp = pprint.PrettyPrinter(indent=4).pprint

from .tasks import (celery_perform_create_product, 
	celery_perform_update_product, celery_perform_delete_product)

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		celery_perform_create_product.delay(serializer.validated_data)
		return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

	def update(self, request, *args, **kwargs):
		partial = kwargs.pop('partial', False)
		instance = self.get_object()
		serializer = self.get_serializer(instance, data=request.data, partial=partial)
		serializer.is_valid(raise_exception=True)
		celery_perform_update_product.delay(instance.id, serializer.validated_data)
		if getattr(instance, '_prefetched_objects_cache', None):
			# If 'prefetch_related' has been applied to a queryset, we need to
			# forcibly invalidate the prefetch cache on the instance.
			instance._prefetched_objects_cache = {}
		return Response(serializer.validated_data)

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		celery_perform_delete_product(instance.id)
		return Response(status=status.HTTP_204_NO_CONTENT)
