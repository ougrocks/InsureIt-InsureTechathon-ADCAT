"""InsureTechathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
<<<<<<< HEAD
from api.views import TruecallerViewSet
from game.views import IndexView, LogoutView, VehicleView, AgentView, AreaView,GameView
=======
from api.views import TruecallerViewSet, GetPolicyQuotes
from game.views import IndexView, LogoutView, VehicleView, AgentView, AreaView
from policycompare.views import PolicyCompareView
>>>>>>> 3f02355e662c03fb0f056677826f2529845a5d4d

router = routers.DefaultRouter()
router.register(r'truecaller', TruecallerViewSet)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^agent/$', AgentView.as_view(), name='agent'),
    url(r'^area/$', AreaView.as_view(), name='area'),
    url(r'^vehicle/$', VehicleView.as_view(), name='vehicle'),
<<<<<<< HEAD
    url(r'^game/$', GameView.as_view(), name='vehicle'),
=======
    url(r'^getquotes/$', GetPolicyQuotes.as_view(), name='getquotes'),
    url(r'^policy/$', PolicyCompareView.as_view(), name='policy'),
>>>>>>> 3f02355e662c03fb0f056677826f2529845a5d4d
    url(r'^api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
