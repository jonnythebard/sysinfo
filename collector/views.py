from rest_framework.viewsets import ModelViewSet

from collector.mixins import InfoViewSet
from collector.models import CpuPerformance, MemoryPerformance, DiskPerformance, ServerInfo, BlackDBPayload
from collector.serializers import CpuPerformanceSerializer, MemoryPerformanceSerializer, DiskPerformanceSerializer,\
    BlackDBPayloadSerializer, ServerInfoSerializer


class CpuPerformanceViewSet(InfoViewSet):
    queryset = CpuPerformance.objects.all()
    serializer_class = CpuPerformanceSerializer


class MemoryPerformanceViewSet(InfoViewSet):
    queryset = MemoryPerformance.objects.all()
    serializer_class = MemoryPerformanceSerializer


class DiskPerformanceViewSet(InfoViewSet):
    queryset = DiskPerformance.objects.all()
    serializer_class = DiskPerformanceSerializer


class ServerInfoViewSet(ModelViewSet):
    queryset = ServerInfo.objects.all()
    serializer_class = ServerInfoSerializer


class BlackDBPayloadViewSet(ModelViewSet):
    queryset = BlackDBPayload.objects.all()
    serializer_class = BlackDBPayloadSerializer
