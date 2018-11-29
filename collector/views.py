from rest_framework import viewsets

from collector.models import CpuInfo, MemoryInfo, DiskInfo
from collector.serializers import CpuInfoSerializer, MemoryInfoSerializer, DiskInfoSerializer


class CpuInfoViewSet(viewsets.ModelViewSet):
    queryset = CpuInfo.objects.all()
    serializer_class = CpuInfoSerializer


class MemoryInfoViewSet(viewsets.ModelViewSet):
    queryset = MemoryInfo.objects.all()
    serializer_class = MemoryInfoSerializer


class DiskInfoViewSet(viewsets.ModelViewSet):
    queryset = DiskInfo.objects.all()
    serializer_class = DiskInfoSerializer
