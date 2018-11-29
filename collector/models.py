from django.db import models


class CpuInfo(models.Model):
    time = models.DateTimeField(primary_key=True)
    user = models.FloatField(default=0)
    nice = models.FloatField(default=0)
    system = models.FloatField(default=0)
    idle = models.FloatField(default=0)
    iowait = models.FloatField(default=0)
    irq = models.FloatField(default=0)
    softirq = models.FloatField(default=0)
    steal = models.FloatField(default=0)
    guest = models.FloatField(default=0)
    guest_nice = models.FloatField(default=0)

    class Meta:
        get_latest_by = "time"


class MemoryInfo(models.Model):
    time = models.DateTimeField(primary_key=True)
    total = models.BigIntegerField(default=0)
    available = models.BigIntegerField(default=0)
    percent = models.FloatField(default=0)
    used = models.BigIntegerField(default=0)
    free = models.BigIntegerField(default=0)
    active = models.BigIntegerField(default=0)
    inactive = models.BigIntegerField(default=0)
    buffers = models.BigIntegerField(default=0)
    cached = models.BigIntegerField(default=0)
    shared = models.BigIntegerField(default=0)
    slab = models.BigIntegerField(default=0)

    class Meta:
        get_latest_by = "time"


class DiskInfo(models.Model):
    time = models.DateTimeField(primary_key=True)
    total = models.BigIntegerField(default=0)
    used = models.BigIntegerField(default=0)
    free = models.BigIntegerField(default=0)
    percent = models.FloatField(default=0)

    class Meta:
        get_latest_by = "time"
