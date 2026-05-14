# autocomplete_views.py

from rest_framework.views import APIView
from rest_framework.response import Response

from .documents import ProductDocument


class ProductAutocompleteView(APIView):

    def get(self, request):
        query = request.GET.get("q", "")

        if not query:
            return Response([])

        search = ProductDocument.search()

        search = search.suggest(
            "product-suggest",
            query,
            completion={
                "field": "suggest",
                "fuzzy": {
                    "fuzziness": 2
                },
                "size": 10,
            }
        )

        response = search.execute()

        suggestions = response.suggest[
            "product-suggest"
        ][0]["options"]

        result = []

        for item in suggestions:
            result.append({
                "text": item["_source"]["title"]
            })

        return Response(result)