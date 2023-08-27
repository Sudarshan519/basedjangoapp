from django.http import Http404
from django.shortcuts import render
from rest_framework import permissions
from website.models import SiteSettingsData
from rest_framework import viewsets,mixins
from rest_framework.response import Response
from website.serializer import SiteSettingsSerializer
# Create your views here.

class SiteViewSet(viewsets.ModelViewSet):
    queryset = SiteSettingsData.objects.all()
    serializer_class = SiteSettingsSerializer
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'retrive':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class SettingsViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    queryset = SiteSettingsData.objects.all()
    serializer_class = SiteSettingsSerializer

    def retrieve_last(self, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())

        try:
            obj =  queryset.latest('Date_Posted')
        except queryset.model.DoesNotExist:
            raise Http404('No %s matches the given query.' \
                          % queryset.model._meta.object_name)

        self.check_object_permissions(self.request, obj)

        serializer = self.get_serializer(obj)

        return Response(serializer.data)