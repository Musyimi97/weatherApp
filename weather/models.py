from django.db import models

# Create your models here.
class Cities(models.Model):
    name= models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class meta:
        verbose_name_plural='cities'

