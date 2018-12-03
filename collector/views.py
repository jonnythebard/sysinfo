from rest_framework import viewsets

from collector.models import CpuPerformance, MemoryPerformance, DiskPerformance
from collector.serializers import CpuPerformanceSerializer, MemoryPerformanceSerializer, DiskPerformanceSerializer


class CpuInfoViewSet(viewsets.ModelViewSet):
    queryset = CpuPerformance.objects.all()
    serializer_class = CpuPerformanceSerializer


class MemoryInfoViewSet(viewsets.ModelViewSet):
    queryset = MemoryPerformance.objects.all()
    serializer_class = MemoryPerformanceSerializer


class DiskInfoViewSet(viewsets.ModelViewSet):
    queryset = DiskPerformance.objects.all()
    serializer_class = DiskPerformanceSerializer
