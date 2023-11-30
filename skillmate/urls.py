from django.contrib import admin
from django.urls import path, include

# main admin paths

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('accounts/', include('allauth.urls')),
]
