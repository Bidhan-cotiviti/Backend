# Generated by Django 4.2.1 on 2023-05-25 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_db_created_at_alter_rd_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='rd',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
