# Generated by Django 2.2.3 on 2019-07-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190718_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='note',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
