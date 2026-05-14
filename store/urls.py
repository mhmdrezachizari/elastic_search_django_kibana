# urls.py

from django.urls import path

from .views import ProductSearchView
from .autocomplete_views import ProductAutocompleteView


urlpatterns = [
    path(
        "search/",
        ProductSearchView.as_view(),
        name="product-search"
    ),

    path(
        "autocomplete/",
        ProductAutocompleteView.as_view(),
        name="product-autocomplete"
    ),
]