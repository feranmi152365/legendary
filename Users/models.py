from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.db import models
from datetime import datetime

# Create your models here.


class MainAmin(models.Model):
    superAdmin = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # userprofile = models.ForeignKey('CustomUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# class MyCustomUserManager(BaseUserManager):
#     def create_user(self, email, username,password=None):
#         if not email:
#             raise ValueError('Users must have an email address')
#         if not username:
#             raise ValueError('Users must have a username')
# 
#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             # surname=surname,
#             # firstname=firstname,
#             # coupon=coupon,
#             # bankName=bankName,
#             # accountName=accountName,
#             # accountNumber=accountNumber,
#         )
# 
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
# 
#     def create_superuser(self, email, username, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             username=username,
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    surname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=20)
    coupon = models.CharField(max_length=100)
    referral = models.CharField(max_length=100, blank=True)
    bankName = models.CharField(max_length=100)
    accountName = models.CharField(max_length=100)
    accountNumber = models.CharField(max_length=100)
    dateRegister = models.DateTimeField(default=datetime.now, blank=True)
#     date_joined = models.DateTimeField(
#         verbose_name='date joined', auto_now_add=True)
#     # last_login = models.DateTimeField(verbose_name='last login', default=True)
#     is_admin = models.BooleanField(default=False)   
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
# 
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
# 
#     objects = MyCustomUserManager()
# 
    def __str__(self):
        return self.username

#     def has_perm(self, perm, obj=None):
#         return self.is_admin
# 
#         # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
#     def has_module_perms(self, app_label):
#         return True
