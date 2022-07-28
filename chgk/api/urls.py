from django.urls import path
from .views import PackagesListView, PackageView


app_name = 'api'
urlpatterns = [
    path('packages/', PackagesListView.as_view()),
    path('packages/<id>', PackageView.as_view()),
]