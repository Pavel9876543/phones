# Generated by Django 4.2.1 on 2023-07-15 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0008_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
    ]
