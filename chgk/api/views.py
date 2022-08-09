# from rest_framework.views import APIView
# from rest_framework.response import Response
from django.http import HttpResponse
import json
from chgk.api.serializers import process_packages_data, process_package_data


def get_test_json(request):
    package = process_package_data('10L_FM_u', 1)
    return HttpResponse(
        json.dumps(package, ensure_ascii=False),
        content_type="application/json"
    )


def get_package_by_id(request, **kwargs):
    if '.' in kwargs['id']:
        package_id, tour_number = kwargs['id'].split('.')
        package = process_package_data(package_id, tour_number)
        return HttpResponse(
            json.dumps(package, ensure_ascii=False),
            content_type="application/json"
        )
    package = process_package_data(kwargs['id'])
    return HttpResponse(
        json.dumps(package, ensure_ascii=False),
        content_type="application/json"
    )


def get_all_packages(request):
    packages = process_packages_data()
    return HttpResponse(
        json.dumps(packages, ensure_ascii=False),
        content_type="application/json"
    )

# WIP
# class PackagesListView(APIView):
#
#     def get(self, request):
#         packages = process_packages_data()
#         return Response(packages)
#
#
# class PackageView(APIView):
#
#     def get(self, request, **kwargs):
#         if '.' in kwargs['id']:
#             package_id, tour_number = kwargs['id'].split('.')
#             package = process_package_data(package_id, tour_number)
#             return Response(package)
#         package = process_package_data(kwargs['id'])
#         return Response(package)
