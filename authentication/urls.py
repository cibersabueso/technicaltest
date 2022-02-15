from django.urls import path, include
from .views import LoginView, LogoutView

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.urls import path, include
from .views import LoginView, LogoutView, SignupView


urlpatterns = [
    
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),
    
]

router = routers.DefaultRouter()

urlpatterns = [
   
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('api/', include(router.urls)),
]

