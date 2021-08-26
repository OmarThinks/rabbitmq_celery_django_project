from .models import (Product)
from .serializers import (ProductSerializer)
from rest_framework import viewsets


from .tasks import celery_perform_create

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def perform_create(self,serializer):
		celery_perform_create.delay(self, serializer)
