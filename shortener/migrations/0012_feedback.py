# Generated by Django 4.2.8 on 2023-12-24 04:46

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0011_alter_stored_url_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=60, validators=[shortener.validators.email_validator])),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
    ]
