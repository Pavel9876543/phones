# Generated by Django 4.2.1 on 2023-07-15 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0005_alter_phones_options_alter_phones_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
