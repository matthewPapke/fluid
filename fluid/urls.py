from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('cal/', include('cal.urls')),
    path('admin/', admin.site.urls),
]