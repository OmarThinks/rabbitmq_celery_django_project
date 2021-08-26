from rest_framework import serializers
from cantiin.models import (Product, Order, Comment)

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = "__all__"
