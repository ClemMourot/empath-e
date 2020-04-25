"""Contact requests related models"""


from django.db import models
from django.contrib.auth.models import User
from app.models.resources import Disorder


class Request(models.Model):
    """Model to store data on contact requests"""

    disorder = models.ForeignKey(Disorder, on_delete=models.CASCADE)
    message = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
