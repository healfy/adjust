from django.db import models


class Metrics(models.Model):

    channel = models.CharField(max_length=100,
                               verbose_name='Channel Name',
                               db_index=True)

    country = models.CharField(max_length=2,
                               verbose_name='Country Name',
                               db_index=True)

    faced_date = models.DateField(verbose_name='Faced Date',
                                  db_index=True)

    os = models.CharField(max_length=100,
                          verbose_name='Operation System Name',
                          db_index=True)

    impressions = models.IntegerField(verbose_name='Impressions count')
    clicks = models.IntegerField(verbose_name='Click count')
    installs = models.IntegerField(verbose_name='Installs count')
    spend = models.FloatField(verbose_name='Spend Count')
    revenue = models.FloatField(verbose_name='Revenue Count')

    def __repr__(self):
        return "<Model{} ({})>".format(self.__class__.__name__, self.id)


