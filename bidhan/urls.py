from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("backend.urls")),
   # path('api/login/',LoginView.as_view(),name='login'),
    path("admin/", admin.site.urls),
]