# Generated by Django 2.1.4 on 2018-12-31 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pst', '0004_auto_20181217_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='text',
            field=models.TextField(),
        ),
    ]
