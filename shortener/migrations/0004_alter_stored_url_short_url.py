# Generated by Django 4.2.2 on 2023-06-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0003_alter_stored_url_short_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stored_url',
            name='short_url',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
