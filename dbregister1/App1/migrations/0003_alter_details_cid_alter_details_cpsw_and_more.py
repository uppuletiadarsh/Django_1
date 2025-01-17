# Generated by Django 5.0.3 on 2024-04-30 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_alter_details_phn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='cid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='details',
            name='cpsw',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='details',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='details',
            name='phn',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='details',
            name='psw',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='details',
            name='qual',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='state',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='details',
            name='uname',
            field=models.CharField(max_length=50),
        ),
    ]
