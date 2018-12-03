from django.db import models


MODEL_CHOICE = (('allinone', '올인원서버'),
                ('manager', '관리서버'),
                ('node', '저장서버'),
                ('nodesensor', '저장 수집서버'),
                ('sensor', '수집서버'))


class ServerInfo(models.Model):
    """
        DPI 서버별 정보
        라이센스 데몬이 해당 정보를 업데이트 한다.
        ID 정보는 라이센스 키에 의해 업데이트 된다.
    """

    id = models.IntegerField(primary_key=True, verbose_name='ID정보')
    name = models.CharField(max_length=32, verbose_name='BlackBox 이름')
    manager_nic = models.CharField(max_length=16, verbose_name="괸리 NIC")
    data_nic = models.CharField(max_length=16, verbose_name="괸리 NIC")
    ipaddr = models.GenericIPAddressField(verbose_name='관리 IP정보')
    ipaddr_data = models.GenericIPAddressField(verbose_name='Data 전송 IP정보')
    hardware_key = models.CharField(max_length=256, verbose_name='하드웨어키')
    host_name = models.CharField(max_length=64, verbose_name='호스트명')
    server = models.CharField(choices=MODEL_CHOICE,
                              max_length=32,
                              verbose_name='확장형일경우 타입정보')
    """ 
        라이센스가 없이 최초 서버가 등록되면 Z

        Y  : 라이센스가 정상적으로 등록되었을경우 
        N : 서버가 삭제되었을경우 
    """
    status = models.CharField(choices=(('uninstalled', '최초 등록'),
                                       ('on', 'ON'),
                                       ('hartbeat_error', 'HeartBeat가 정상이 아님'),
                                       ('license_error', '라이센스 등록안됨')),
                              max_length=32,
                              verbose_name='상태정보')
    """
        License 데몬이 업데이트 한다.
        5분동안 업데이트 되지 않으면 서버가 죽은것으로 간주한다.. ( 라이센스 데몬이 체크 ) 
    """
    status_date = models.DateTimeField(auto_now_add=True, verbose_name="상태 업데이트 시간")

    class Meta:
        verbose_name_plural = "1_서버 기본 정보"
        db_table = 'server_info'

    def __str__(self):
        return "{0} {1}".format(self.name, self.ipaddr)


class CpuPerformance(models.Model):
    time = models.DateTimeField(primary_key=True)
    # server = models.ForeignKey(ServerInfo, on_delete=models.CASCADE)
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


class MemoryPerformance(models.Model):
    time = models.DateTimeField(primary_key=True)
    # server = models.ForeignKey(ServerInfo, on_delete=models.CASCADE)
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


class DiskPerformance(models.Model):
    time = models.DateTimeField(primary_key=True)
    # server = models.ForeignKey(ServerInfo, on_delete=models.CASCADE)
    total = models.BigIntegerField(default=0)
    used = models.BigIntegerField(default=0)
    free = models.BigIntegerField(default=0)
    percent = models.FloatField(default=0)

    class Meta:
        get_latest_by = "time"


class BlackDBPayload(models.Model):
    """
        Payload 파일 정보
    """
    id = models.BigAutoField(primary_key=True)
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='생성시간')
    server = models.ForeignKey(ServerInfo, on_delete=models.CASCADE)
    thread = models.IntegerField(verbose_name='Parser Thread 번호')
    size = models.BigIntegerField(verbose_name='Payload 파일 사이즈')

    parser_flag = models.CharField(max_length=1,
                                   default="N",
                                   choices=(("Y", '파싱됨'),
                                            ("N", '파싱안됨')),
                                   verbose_name="상태정보")

    contents_flag = models.CharField(max_length=1,
                                     default="N",
                                     choices=(("Y", '컨텐츠까지 파싱'),
                                              ("F", '파일추출함'),
                                              ("N", '파싱안함')),
                                     verbose_name='컨텐츠 추출 여부')

    post_flag = models.CharField(max_length=1,
                                 default="N",
                                 choices=(("Y", '파싱함'), ("N", '파싱안함')),
                                 verbose_name='POST 추출 여부 전송여부')

    send_flag = models.CharField(max_length=1,
                                 default="N",
                                 choices=(("Y", '전송함'),
                                          ("N", '전송전'),
                                          ("F", "FILE 없음")),
                                 verbose_name='분산형일경우 전송여부')

    class Meta:
        unique_together = ('create_date', 'server', 'thread')
        db_table = 'black_database_payload'
