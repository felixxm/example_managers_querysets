from datetime import date, timedelta

from django.db import models
from django.db.models.functions import Concat


class PersonQuerySet(models.QuerySet):
    def with_extra_fields(self):
        return self.annotate(
            full_name=Concat("first_name", models.Value(" "), "last_name"),
        )

    def experienced(self):
        return self.filter(join_date__lt=date.today() - timedelta(days=1000))

    def number_of_unique_names(self):
        return self.aggregate(
            count=models.Count("last_name", distinct=True),
        )["count"]
