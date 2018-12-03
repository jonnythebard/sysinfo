from rest_framework import serializers
from collector.models import CpuPerformance, MemoryPerformance, DiskPerformance


class CpuPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuPerformance
        fields = ('time', 'user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'guest', 'guest_nice')


class MemoryPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryPerformance
        fields = ('time', 'total', 'available', 'percent', 'used', 'free', 'active', 'inactive', 'buffers', 'cached',
                  'shared', 'slab')


class DiskPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskPerformance
        fields = ('time', 'total', 'used', 'free', 'percent')
