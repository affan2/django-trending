import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Sum
from django.conf import settings

from django.contrib.contenttypes.models import ContentType


class TrendingManager(models.Manager):

    def trending(self, model, days=30, kind=""):
        views = self.filter(
            viewed_content_type=ContentType.objects.get_for_model(model),
            views_on__gte=datetime.date.today() - datetime.timedelta(days=days),
            kind=kind,
            site_id=settings.SITE_ID
        ).values(
            "viewed_content_type",
            "viewed_object_id",
            "kind"
        ).annotate(
            num_views=Sum("count")
        ).order_by("-num_views")[:50]

        for d in views:
            try:
                d["object"] = ContentType.objects.get_for_id(
                    d["viewed_content_type"]
                ).get_object_for_this_type(
                    pk=d["viewed_object_id"]
                )
            except ObjectDoesNotExist:
                d["object"] = None
        return views
