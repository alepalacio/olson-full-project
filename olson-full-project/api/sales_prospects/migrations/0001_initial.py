# Generated by Django 4.0.3 on 2022-04-17 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesProspectsProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_user', models.CharField(max_length=100)),
                ('full_name', models.CharField(default=None, max_length=100)),
                ('amount', models.FloatField()),
                ('phone', models.CharField(max_length=14)),
                ('call', models.CharField(max_length=255)),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner_prospect', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
