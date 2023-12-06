# artist_api/urls.py
from django.urls import path
from .views import WorkListCreateView, ArtistSearchView, ArtistWorkListView, register_user
from .views import register_user
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('api/works/', WorkListCreateView.as_view(), name='work-list-create'),
    path('api/works?work_type=<str:work_type>/', WorkListCreateView.as_view(), name='work-list-filter'),
    path('api/works?artist=<str:artist_name>/', ArtistWorkListView.as_view(), name='artist-work-list'),
    # path('api/register/', register_user, name='register-user'),
    # path('api/register/', register_user, name='register-user'),
    # path('admin/', admin.site.urls),
    # path('api/', include('artist_api.urls')),
    path('api/register/', register_user, name='register-user'),
    path('admin/', admin.site.urls),
    path('api/', include('artist_api.urls')),
]

# artist_api/urls.py

