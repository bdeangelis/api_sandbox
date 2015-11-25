from django.conf.urls import url, include
from rest_framework import routers
from tutorial.quickstart import views

router = router.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatters = [
    url(r'^', include(router.urls)),
    url(r'^api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
