from rest_framework import serializers
from collector.models import CpuInfo, MemoryInfo, DiskInfo


class CpuInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuInfo
        fields = ('time', 'user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'guest', 'guest_nice')


class MemoryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryInfo
        fields = ('time', 'total', 'available', 'percent', 'used', 'free', 'active', 'inactive', 'buffers', 'cached',
                  'shared', 'slab')


class DiskInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskInfo
        fields = ('time', 'total', 'used', 'free', 'percent')
