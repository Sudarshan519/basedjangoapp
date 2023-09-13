from django.http import Http404, JsonResponse
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
        print(self.action)
        if self.action == 'retrieve' or  self.action=='list':
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
    
from drf_yasg.utils import swagger_auto_schema 
from rest_framework.decorators import api_view
from rest_framework.request import Request
from drf_yasg import openapi
@swagger_auto_schema(methods=['get'], operation_description="description", manual_parameters=[
    # openapi.Parameter('category', openapi.IN_QUERY, "category1, category2, category3", type=openapi.TYPE_STRING),
    # openapi.Parameter('name', openapi.IN_QUERY, "full name", type=openapi.TYPE_STRING),
], responses={
    200: openapi.Response('Response', SiteSettingsSerializer),
}, tags=['Site Setting'])
# @swagger_auto_schema(tags=['user'],method='GET', operation_description='',request_body=SiteSettingsSerializer)
@api_view(['GET' ])
def sitedetail(request):
    """
    List all code snippets, or create a new snippet.
    """
    serializer_context = {
    'request':  (request),
    }
    # last_object = Object.objects.order_by('-timestamp_field').last()
    try:

        snippets = SiteSettingsData.objects.latest('id')
        serializer = SiteSettingsSerializer(snippets, many=False,context=serializer_context)
        return Response(serializer.data)
    except Exception as e:
        return JsonResponse({
            "status_code":"500",
            "detail":"No Site settings found"})