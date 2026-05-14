from django.urls import path
from .views import StoreView
urlpatterns = [
    path('get/' , StoreView.as_view()),
]