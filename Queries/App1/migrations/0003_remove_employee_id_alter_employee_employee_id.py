# Generated by Django 5.0.3 on 2024-05-24 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_remove_employee_languages_known_delete_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]