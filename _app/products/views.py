from .models import (Product)
from .serializers import (ProductSerializer)
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

	def perform_create(self,serializer):
		print("Creating", flush=True)
		return viewsets.ModelViewSet.perform_create(self,serializer)
