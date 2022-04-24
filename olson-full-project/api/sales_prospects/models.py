from django.db import models
from users.models import User

# Create your models here.

class SalesProspectProfile(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    owner = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, related_name="owner_prospect", verbose_name='owner'
    )
    fb_user = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100, blank=True, default=None)
    amount = models.CharField(max_length=11)
    phone = models.CharField(max_length=14)
    call = models.CharField(max_length=255)
    nss = models.CharField(max_length=11, null=True, blank=True, default="")
    first_credit = models.BooleanField(default=True)
    called = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        db_table = 'sales_prospects'
        verbose_name = 'Sales Prospect'
        verbose_name_plural = 'Sales Prospects'

    def __str__(self):
        return self.fb_user




