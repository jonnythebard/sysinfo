database = {
        'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=sysinfoschema'
        },
        'NAME': 'sysinfo',
        'USER': 'sysinfo',
        'PASSWORD': '123123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

secret_key = 'i5w%$(rkh-vvy6hqc2r=_z8ajd017^31r!i-6u2lfoeoyhy!78'
