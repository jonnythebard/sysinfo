from django.urls import path, include
from rest_framework.routers import DefaultRouter
from collector import views

router = DefaultRouter()
router.register(r'CpuPerformance', views.CpuInfoViewSet)
router.register(r'MemoryPerformance', views.MemoryInfoViewSet)
router.register(r'DiskPerformance', views.DiskInfoViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
