from django.core.management.base import BaseCommand
from sysinfo.config import database
import psycopg2

database = database['default']


class Command(BaseCommand):
    help = 'Create hypertables'

    def add_arguments(self, parser):
        parser.add_argument('--schema', type=str)
        parser.add_argument('--app_label', type=str)

    def handle(self, *args, **options):
        schema = options['schema']
        app_label = options['app_label']

        if not schema:
            schema = database['OPTIONS']['options'].split('=')[1]

        if not app_label:
            app_label = 'collector'

        conn = psycopg2.connect(dbname=database['NAME'],
                                user=database['USER'],
                                password=database['PASSWORD'],
                                host=database['HOST'],
                                port=database['PORT'],
                                options=database['OPTIONS']['options'])
        cur = conn.cursor()

        cur.execute(f"SELECT tablename FROM pg_tables WHERE schemaname='{schema}' AND tablename LIKE '{app_label}_%'")
        all_tables = set([table[0] for table in cur.fetchall()])

        cur.execute("SELECT table_name FROM _timescaledb_catalog.hypertable")
        hypertables = set([table[0] for table in cur.fetchall()])

        tables = all_tables - hypertables

        if not tables:
            print("no table to create")
            return

        for table in tables:
            print(f"create hypertable: {table}")
            try:
                cur.execute(f"SELECT create_hypertable('{table}'::regclass ,'time'::name);")
            except Exception as e:
                print(e)

        conn.commit()

        cur.close()
        conn.close()

