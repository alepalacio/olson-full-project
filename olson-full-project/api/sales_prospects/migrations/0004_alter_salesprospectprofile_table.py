# Generated by Django 4.0.3 on 2022-04-17 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales_prospects', '0003_salesprospectprofile_delete_salesprospectsprofile'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='salesprospectprofile',
            table='sales_prospects',
        ),
    ]