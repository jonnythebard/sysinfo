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
        ordering = ('-time',)


class MemoryInfo(models.Model):
    time = models.DateTimeField(primary_key=True)
    total = models.IntegerField(default=0)
    available = models.IntegerField(default=0)
    percent = models.FloatField(default=0)
    used = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    active = models.IntegerField(default=0)
    inactive = models.IntegerField(default=0)
    buffers = models.IntegerField(default=0)
    cached = models.IntegerField(default=0)
    shared = models.IntegerField(default=0)
    slab = models.IntegerField(default=0)

    class Meta:
        ordering = ('-time',)


class DiskInfo(models.Model):
    time = models.DateTimeField(primary_key=True)
    total = models.IntegerField(default=0)
    used = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    percent = models.FloatField(default=0)

    class Meta:
        ordering = ('-time',)
