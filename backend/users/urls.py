from . import views
from rest_framework_nested import routers
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r"test_kits", views.TestKitViewSet, basename="test_kits")
router.register(r"users", views.CreateProfileViewSet, basename="profile")

urlpatterns = [
    path("api/", include(router.urls)),
]