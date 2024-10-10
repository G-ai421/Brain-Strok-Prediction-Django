
from django.urls import path
from .views import home, predict  # Import views directly
from . import views
urlpatterns = [

    path('', home, name='home'),
    # path('predict/', predict, name='predict'),
    path('predict/', views.predict, name='predict'), 
    
]   
  
