from __future__ import annotations
from django.db import models, transaction
from django.db.models import QuerySet

from ampa_members_manager.activity.models.single_activity import SingleActivity


class NoSingleActivityError(Exception):
    def __init__(self):
        super().__init__("NoSingleActivityError")


class ChargeGroup(models.Model):
    single_activities = models.ManyToManyField(to=SingleActivity)

    @classmethod
    def create_filled_charge_group(cls, single_activities: QuerySet[SingleActivity]) -> ChargeGroup:
        if not single_activities.exists():
            raise NoSingleActivityError

        with transaction.atomic():
            charge_group: ChargeGroup = ChargeGroup.objects.create()
            charge_group.single_activities.set(single_activities)
            return charge_group
