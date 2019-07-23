from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

class Resource(models.Model):

    # We do not create a separate resource_id field because
    # it is automatically created by Django
    # see docs here: https://docs.djangoproject.com/en/2.2/topics/db/models/#automatic-primary-key-fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    url = models.URLField(max_length=200) # Default value is 200
    note = models.CharField(max_length=300, blank=True, null=True)

    # ArrayField is a Postgres only field (check the import)
    # Docs here: https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/#arrayfield
    tags = ArrayField(models.CharField(max_length=60), blank=True, null=True)

    date_of_creation = models.DateField(auto_now=True) # Automatically set field every time an object is created

    def __str__(self):
        return f"[{self.user}] {self.title}"