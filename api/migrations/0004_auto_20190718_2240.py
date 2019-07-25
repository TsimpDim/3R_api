# Generated by Django 2.2.3 on 2019-07-18 19:40

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_remove_resource_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='user_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resource',
            name='note',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='resource',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=60), null=True, size=None),
        ),
    ]