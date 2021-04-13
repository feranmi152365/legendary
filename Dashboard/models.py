from django.db import models
from Users.models import CustomUser
from .utils import generate_ref_code

# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=50)
    ReferralEarning = models.CharField(max_length=50)
    ActivitiesEarning = models.CharField(max_length=50)
    Package = models.CharField(max_length=50)
    NextWithdraw = models.DateField(auto_now_add=False)
    UnpaidReferral = models.CharField(max_length=20)
    PaidReferral = models.CharField(max_length=20)
    CurrentReferral = models.CharField(max_length=20)
    TotalReferral = models.CharField(max_length=20)
    Cycles = models.CharField(max_length=20)
    PreviousReferral = models.CharField(max_length=20)
    AvailableEarning = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Refferal(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    code = models.CharField(max_length=12, blank=True)
    recommended_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, related_name='ref_by')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code
        # return f"{self.user.username}-{self.code}"
    
    def get_recommened_refferals(self):
        qs = Refferal.objects.all()

        my_resc =[]
        for refferal in qs:
            if refferal.recommended_by == self.user:
                my_resc.append(refferal)
        return my_resc

    def save(self, *args, **kwargs):
        if self.code =='':
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)