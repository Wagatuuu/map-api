# Generated by Django 4.1 on 2022-09-19 16:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0003_alter_useruploadeddata_noiselevel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useruploadeddata',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
