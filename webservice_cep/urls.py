from django.conf.urls import url, include
from rest_framework import routers
from apps.core import views as core_views

router = routers.DefaultRouter()
router.register(r'^', core_views.ZipcodeViewSet)

urlpatterns = [
    url(r'^$', core_views.Home.as_view(), name='home'),
    url(r'^zipcode', include(router.urls)),
]
