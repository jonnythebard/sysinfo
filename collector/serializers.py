from rest_framework import serializers
from collector.models import CpuPerformance, MemoryPerformance, DiskPerformance, ServerInfo, BlackDBPayload


class ServerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInfo
        fields = ('server_id', 'name', 'manager_nic', 'data_nic', 'ipaddr', 'ipaddr_data', 'hardware_key', 'host_name',
                  'server')


class BlackDBPayloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackDBPayload
        fields = ('payload_id', 'create_date', 'server', 'thread', 'size', 'parser_flag', 'contents_flag', 'post_flag',
                 'send_flag')


class CpuPerformanceSerializer(serializers.ModelSerializer):
    # server = ServerInfoSerializer(read_only=True)

    class Meta:
        model = CpuPerformance
        fields = ('time', 'user', 'nice', 'system', 'idle', 'iowait', 'irq', 'softirq', 'steal', 'guest',
                  'guest_nice')


class MemoryPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemoryPerformance
        fields = ('time', 'total', 'available', 'percent', 'used', 'free', 'active', 'inactive', 'buffers',
                  'cached', 'shared', 'slab')


class DiskPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskPerformance
        fields = ('time', 'total', 'used', 'free', 'percent')
