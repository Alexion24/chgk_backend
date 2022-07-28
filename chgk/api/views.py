from rest_framework.views import APIView
from rest_framework.response import Response
from chgk.api.serializers import process_packages_data, process_package_data


class PackagesListView(APIView):

    def get(self, request):
        packages = process_packages_data()
        return Response(packages)


class PackageView(APIView):

    def get(self, request, **kwargs):
        package = process_package_data(kwargs['id'])
        return Response(package)
