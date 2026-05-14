# views.py

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from elasticsearch_dsl import Q

from .documents import ProductDocument
from .serializers import ProductSearchSerializer


@method_decorator(cache_page(60 * 2), name='dispatch')
class ProductSearchView(APIView):

    def get(self, request):
        query = request.GET.get("q", "")
        ordering = request.GET.get("ordering", "newest")

        min_price = request.GET.get("min_price")
        max_price = request.GET.get("max_price")

        page = int(request.GET.get("page", 1))
        size = int(request.GET.get("size", 20))

        start = (page - 1) * size
        end = start + size

        search = ProductDocument.search()

        # only active products
        search = search.filter(
            "term",
            is_active=True
        )

        # full text search
        if query:
            q = Q(
                "multi_match",
                query=query,
                fields=[
                    "title^5",
                    "description^2",
                ],
                fuzziness="AUTO",
            )

            search = search.query(q)

        # price filters
        if min_price:
            search = search.filter(
                "range",
                price={
                    "gte": int(min_price)
                }
            )

        if max_price:
            search = search.filter(
                "range",
                price={
                    "lte": int(max_price)
                }
            )

        # ordering
        if ordering == "cheap":
            search = search.sort("price")

        elif ordering == "expensive":
            search = search.sort("-price")

        elif ordering == "oldest":
            search = search.sort("created_at")

        else:
            search = search.sort("-created_at")

        # pagination
        search = search[start:end]

        response = search.execute()

        products = []

        for hit in response:
            products.append({
                "id": hit.id,
                "title": hit.title,
                "description": getattr(hit, "description", ""),
                "price": hit.price,
                "is_active": hit.is_active,
                "created_at": hit.created_at,
            })

        serializer = ProductSearchSerializer(
            products,
            many=True
        )

        return Response({
            "count": response.hits.total.value,
            "page": page,
            "size": size,
            "results": serializer.data,
        }, status=status.HTTP_200_OK)