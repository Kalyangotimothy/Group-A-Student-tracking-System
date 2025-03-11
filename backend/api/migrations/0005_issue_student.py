# Generated by Django 5.1.6 on 2025-03-11 05:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_courseunit_alter_customuser_role_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='student',
            field=models.ForeignKey(limit_choices_to={'Role': 'Student'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to=settings.AUTH_USER_MODEL),
        ),
    ]
