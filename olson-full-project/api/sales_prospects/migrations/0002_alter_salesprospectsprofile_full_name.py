# Generated by Django 4.0.3 on 2022-04-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_prospects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesprospectsprofile',
            name='full_name',
            field=models.CharField(blank=True, default=None, max_length=100),
        ),
    ]