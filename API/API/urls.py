
from django.contrib import admin
from django.urls import path,include
 # Import views directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("APP.urls"))
]
