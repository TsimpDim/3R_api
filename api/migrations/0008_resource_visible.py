# Generated by Django 2.2.3 on 2019-07-27 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190721_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='visible',
            field=models.BooleanField(default=True),
        ),
    ]
