from typing import List, Final

from django.test import TestCase
from model_bakery import baker

from ampa_members_manager.academic_course.models.active_course import ActiveCourse
from ampa_members_manager.activity.models.single_activity import SingleActivity
from ampa_members_manager.activity_registration.models.activity_registration import ActivityRegistration
from ampa_members_manager.charge.models.charge import Charge
from ampa_members_manager.charge.models.charge_group import ChargeGroup
from ampa_members_manager.family.models.bank_account import BankAccount
from ampa_members_manager.tests.generator_adder import GeneratorAdder

GeneratorAdder.add_all()


class TestCharge(TestCase):
    @classmethod
    def setUpTestData(cls):
        ActiveCourse.objects.create(course=baker.make('AcademicCourse'))

    def test_create_charges_activity_registrations_different_bank_accounts(self):
        count: Final[int] = 3
        activity_registrations: List[ActivityRegistration] = baker.make('ActivityRegistration', _quantity=count)
        charge_group: ChargeGroup = ChargeGroup.create_filled_charge_group(SingleActivity.objects.all())

        Charge.create_charges(charge_group)

        self.assertEqual(count, Charge.objects.count())
        for activity_registration in activity_registrations:
            amount = activity_registration.single_activity.calculate_price(
                times=activity_registration.amount, membership=activity_registration.is_membership())
            Charge.objects.get(activity_registrations__exact=activity_registration, amount=amount)

    def test_create_charges_activity_registrations_same_bank_accounts(self):
        count: Final[int] = 3
        bank_account: BankAccount = baker.make('BankAccount')
        activity_registrations: List[ActivityRegistration] = baker.make(
            'ActivityRegistration', _quantity=count, bank_account=bank_account)
        charge_group: ChargeGroup = ChargeGroup.create_filled_charge_group(SingleActivity.objects.all())

        Charge.create_charges(charge_group)

        self.assertEqual(1, Charge.objects.count())
        charge = Charge.objects.first()
        self.assertEqual(activity_registrations, list(charge.activity_registrations.all()))
        amount = 0
        for activity_registration in activity_registrations:
            amount += activity_registration.single_activity.calculate_price(
                times=activity_registration.amount, membership=activity_registration.is_membership())
        self.assertEqual(amount, charge.amount)

    def test_create_filled_charges_activity_registrations_same_bank_accounts(self):
        count: Final[int] = 3
        baker.make('ActivityRegistration', _quantity=count, bank_account=baker.make('BankAccount'))

        Charge.create_filled_charges(SingleActivity.objects.all())

        self.assertEqual(1, Charge.objects.count())