from django.db import models
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator


class Coupon(models.Model):
    code = models.CharField(max_length=50,
                            unique=True)
    valid_from = models.DateField()
    valid_to = models.DateField()
    package = models.IntegerField( validators=[MinValueValidator(5000),
                                               MaxValueValidator(100000)])
    active = models.BooleanField()

    def __str__(self):
        return self.code
