# Generated by Django 5.0.3 on 2024-05-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('idno', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
