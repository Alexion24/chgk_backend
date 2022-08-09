from django.urls import path
from .views import PackagesListView, PackageView, get_test_json


app_name = 'api'
urlpatterns = [
    path('packages/', PackagesListView.as_view()),
    path('packages/<id>', PackageView.as_view()),
    path('', get_test_json),
]