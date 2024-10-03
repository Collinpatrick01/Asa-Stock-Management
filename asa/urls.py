from django.contrib import admin
from django.urls import path, include
import lowbudget.urls as lowbudget_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(lowbudget_urls)),
    path("accounts/", include("django.contrib.auth.urls")),
    
]
