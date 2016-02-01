from django.conf.urls import url, include
from rest_framework import routers
from apps.core import views as core_views

router = routers.DefaultRouter()
router.register(r'zipcode', core_views.ZipcodeViewSet)
router.register(r'log/(?P<zip_code>\d{8})', core_views.LogViewSet)

urlpatterns = [
    url(r'^$', core_views.Home.as_view(), name='home'),
    url(r'^', include(router.urls)),
]
