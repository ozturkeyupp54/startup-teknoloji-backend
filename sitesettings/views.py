from rest_framework import viewsets, status
from rest_framework.response import Response

from sitesettings.models import SiteSettings
from sitesettings.serializers import SiteSettingsSerializer
from utils.permissions import IsAdminOrReadOnly


class SiteSettingsViewSet(viewsets.ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
    permission_classes = [IsAdminOrReadOnly]
    ordering = ['-pk']

    def get_queryset(self):
        order_by = self.request.query_params.get('order_by', '-id')
        return SiteSettings.objects.all().order_by(order_by)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                {"status": True,
                 "message": "SiteSettings successfully created.",
                 "data": serializer.data},
                status=status.HTTP_201_CREATED, headers=headers)
        return Response(
            {"status": False,
             "message": "SiteSettings creation failed.",
             "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            return Response(
                {"status": True,
                 "message": "SiteSettings successfully updated.",
                 "data": serializer.data},
                status=status.HTTP_200_OK)
        return Response(
            {"status": False,
             "message": "SiteSettings update failed.",
             "data": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"status": True,
             "message": "SiteSettings successfully deleted.",
             "data": []},
            status=status.HTTP_200_OK)
