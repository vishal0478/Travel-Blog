# Generated by Django 3.0.4 on 2020-10-11 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='listing',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]