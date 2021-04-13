from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    list_display = ['id','username', 'email','phoneNumber','coupon']
    list_display_links = ['id','username', 'email']

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('surname','firstname','coupon','email','phoneNumber','referral','bankName','accountName','accountNumber','dateRegister')}),
    )
    fieldsets = UserAdmin.fieldsets+ (
        (None, {'fields': ('coupon','phoneNumber','referral','bankName','accountName','accountNumber','dateRegister')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)