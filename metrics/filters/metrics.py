import dataclasses
from typing import Optional

from django.db.models import QuerySet


@dataclasses.dataclass
class MetricsFilter:
    date_from: Optional[str]
    date_to: Optional[str]
    country: Optional[str]
    os: Optional[str]
    channel: Optional[str]

    def filter_queryset(self, queryset: QuerySet):

        if self.date_from is not None and self.date_to is not None:
            queryset = queryset.filter(
                faced_date__range=[self.date_from, self.date_to])
        elif self.date_from is not None:
            queryset = queryset.filter(faced_date__gte=self.date_from)
        elif self.date_to is not None:
            queryset = queryset.filter(faced_date__lte=self.date_to)

        if self.channel is not None:
            queryset = queryset.filter(channel=self.channel)

        if self.os is not None:
            queryset = queryset.filter(os=self.os)
        if self.country is not None:
            queryset = queryset.filter(country=self.country)

        return queryset
