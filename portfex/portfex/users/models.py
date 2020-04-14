from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, DateField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), max_length=255,)
    dob = DateField("Date of Birth", null=True,)
    address = CharField("Address", max_length=255, null=True,)
    town_or_city = CharField("Town/City", max_length=64, null=True,)
    zipcode = CharField("Zipcode/Postcode", max_length=32, null=True,)
    country = CountryField("Country", max_length=64)
    tax_residency = CharField("Tax Residency", max_length=32, blank=True, null=True,)
    kyc_last_date = DateField("Last KYC Check", blank=True, null=True,)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
