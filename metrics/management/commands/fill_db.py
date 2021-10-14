import csv
import datetime
from django.conf import settings
from django.core.management.base import BaseCommand

from metrics.models import Metrics


class Command(BaseCommand):
    help = 'create metrics'

    def handle(self, *args, **options):
        with open(settings.DATASET_PATH, "rt") as fin:
            for i in csv.DictReader(fin):
                p = Metrics(
                    faced_date=i['date'],
                    country=i['country'],
                    channel=i['channel'],
                    os=i['os'],
                    impressions=i['impressions'],
                    clicks=i['clicks'],
                    installs=i['installs'],
                    spend=i['spend'],
                    revenue=i['revenue'])
                p.save()
        print('Fill db is finished')
