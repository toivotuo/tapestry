# Generated by Django 3.1.2 on 2020-11-28 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settler', '0005_auto_20200921_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transfer',
            name='account',
        ),
        migrations.RemoveField(
            model_name='transfer',
            name='transaction',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='Transfer',
        ),
    ]