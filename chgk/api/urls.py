from django.urls import path
from .views import get_test_json, get_package_by_id, get_all_packages


app_name = 'api'
urlpatterns = [
    # WIP
    # path('packages/', PackagesListView.as_view()),
    # path('packages/<id>', PackageView.as_view()),
    path('packages/', get_all_packages),
    path('packages/<id>', get_package_by_id),
    path('', get_test_json),
]