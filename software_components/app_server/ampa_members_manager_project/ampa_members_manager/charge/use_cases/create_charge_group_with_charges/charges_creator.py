from typing import List

from ampa_members_manager.activity_registration.models.activity_registration import ActivityRegistration
from ampa_members_manager.charge.models.charge import Charge, NotFound
from ampa_members_manager.charge.models.charge_group import ChargeGroup


class ChargesCreator:
    def __init__(self, charge_group: ChargeGroup):
        self.__charge_group: ChargeGroup = charge_group

    def create(self):
        activity_registrations: List[ActivityRegistration] = []
        for single_activity in self.__charge_group.single_activities.all():
            activity_registrations.extend(ActivityRegistration.with_single_activity(single_activity=single_activity))
        for activity_registration in activity_registrations:
            self.__create_charge_for_activity_registration(activity_registration)

    def __create_charge_for_activity_registration(self, activity_registration: ActivityRegistration):
        charge: Charge = self.__find_or_create_charge(activity_registration)
        charge.activity_registrations.add(activity_registration)
        charge.save()

    def __find_or_create_charge(self, activity_registration: ActivityRegistration) -> Charge:
        try:
            return Charge.find_charge_with_bank_account(bank_account=activity_registration.bank_account)
        except NotFound:
            price: float = activity_registration.single_activity.calculate_price(
                times=activity_registration.amount, membership=activity_registration.is_membership())
            return Charge.objects.create(group=self.__charge_group, amount=price)
