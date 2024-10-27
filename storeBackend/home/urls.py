from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ItemsViewset

router = DefaultRouter()
router.register(r'items', ItemsViewset, basename='items')
# urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
]
