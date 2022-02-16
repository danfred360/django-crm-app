from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('maria/', include('meals.urls')),
    path('admin/', admin.site.urls),
]
