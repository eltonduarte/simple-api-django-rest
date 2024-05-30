from django.db import models

# Model é a representação de algum objeto.
class Users(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)