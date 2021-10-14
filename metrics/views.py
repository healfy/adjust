from django.db.models import Sum, FloatField, F, Count
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from metrics.filters import MetricsFilter
from metrics.models import Metrics


class MetricView(ListAPIView):

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        return Response([_ for _ in queryset])

    def get_queryset(self):
        queryset = Metrics.objects.extra(
            select={'cpi': 'SELECT (SUM("metrics_metrics"."spend")/ SUM("metrics_metrics"."installs")) AS "cpi" FROM "metrics_metrics"'}
        )

        sums = self.request.query_params.get('sums', None)
        group_by = self.request.query_params.get('groupby', None)
        ordering = self.request.query_params.get('ordering', None)
        country = self.request.query_params.get('country', None)
        os = self.request.query_params.get('os', None)
        channel = self.request.query_params.get('channel', None)
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)
        flt = MetricsFilter(date_from, date_to, country, os, channel)
        queryset = flt.filter_queryset(queryset)
        if group_by and sums:
            groupby = set(group_by.split(','))
            queryset = queryset.values(*groupby)
            for field_name in set(sums.split(',')):
                queryset = queryset.annotate(
                    **{f'{field_name}_count': Sum(field_name)}
                )

        if ordering:
            queryset = queryset.order_by(ordering)
        return queryset
