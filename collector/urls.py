from django.urls import path, include
from rest_framework_nested.routers import SimpleRouter, NestedSimpleRouter
from collector import views

performance_router = SimpleRouter()
performance_router.register(r'performance', views.ServerInfoViewSet)

blackdb_router = SimpleRouter()
blackdb_router.register(r'blackdb', views.BlackDBPayloadViewSet)

info_router = NestedSimpleRouter(performance_router, r'performance', lookup='performance')
info_router.register(r'cpu', views.CpuPerformanceViewSet)
info_router.register(r'memory', views.MemoryPerformanceViewSet)
info_router.register(r'disk', views.DiskPerformanceViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(performance_router.urls)),
    path('', include(blackdb_router.urls)),
    path('', include(info_router.urls))
]
