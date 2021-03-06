"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from cars.views import UserViewSet, CarViewSet
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'cars', CarViewSet, basename="car")
urlpatterns = router.urls

urlpatterns = [
    url(r'^api/', include(router.urls)),
    path('api/auth/', obtain_auth_token, name='api-token-auth'),
    path('api/register/', UserViewSet.as_view({'post': 'create'})),
    path('api/update/<int:pk>', UserViewSet.as_view({'put': 'update'})),
]
