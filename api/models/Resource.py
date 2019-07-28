from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from api.validators import validate_no_duplicates

class Resource(models.Model):

    # We do not create a separate resource_id field because
    # it is automatically created by Django
    # see docs here: https://docs.djangoproject.com/en/2.2/topics/db/models/#automatic-primary-key-fields
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120,
        validators=[RegexValidator(
            regex=r"^[A-Za-z0-9_ \u0370-\u03ff\u1f00-\u1fff]*$",
            message="Title contains invalid characters.",
            code="inv_char"
        )]
    )

    url = models.URLField(max_length=200) # Default max_length is 200
    note = models.CharField(max_length=300, blank=True, null=False, default=str)

    # ArrayField is a Postgres only field (check the import)
    # Docs here: https://docs.djangoproject.com/en/1.11/ref/contrib/postgres/fields/#arrayfield
    tags = ArrayField(
        models.CharField(
            max_length=60,
            blank=True,
            null=False,
            validators=[ # Validator for every CharField in array
                RegexValidator(
                    regex=r"^[A-Za-z0-9_ \u0370-\u03ff\u1f00-\u1fff]*$",
                    message="Tags contain invalid characters."
                )
            ]
        ),
        validators=[validate_no_duplicates], # Validator for the ArrayField as a whole
        default=list
    )

    date_of_creation = models.DateField(auto_now=True) # Automatically set field every time an object is created
    
    visible = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.user}] {self.title}"