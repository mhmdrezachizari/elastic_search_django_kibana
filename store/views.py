from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer




@method_decorator(cache_page(60 * 5), name='dispatch')  # 5 minutes
class StoreView(ListAPIView):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

