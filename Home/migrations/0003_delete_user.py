# Generated by Django 5.1.4 on 2025-01-05 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_remove_lga_state_alter_schoolregistration_email_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
