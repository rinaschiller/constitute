# Generated by Django 2.0.2 on 2018-12-17 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pst', '0003_remove_tweet_dummy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='sentiment',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
