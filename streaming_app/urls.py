from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet,basename="snippet")
# router.register(r'users', views.UserViewSet,basename="user")
router.register('movies',views.MovieViewSet,basename="movies")
router.register("tvshows",views.TVShowsViewSet,basename="tvshows")
router.register("episode-list",views.EpisodesViewSet,basename="episode")

# router.register(r'documents',views.ProfileDocumentViewset,basename='profileDocuments')
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("user",views.UserDashboard.as_view(),),
    path('streaming', include(router.urls)),
     path('',include('userr.urls')),
    path('',include("subscription.urls")),
        path('homeapi', views.HomeAPI.as_view(), name='home-api'),
        path('watchMovie/<str:id>',views.WatchMovieAPI.as_view()),
         path('stream/<int:file_id>/', views.stream_file, name='stream_file'),
]