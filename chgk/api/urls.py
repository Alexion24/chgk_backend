from django.urls import path
from .views import PackageView, PackagesListView

app_name = 'api'
urlpatterns = [
    path('packages/', PackagesListView.as_view()),
    path('packages/<id>', PackageView.as_view()),
]