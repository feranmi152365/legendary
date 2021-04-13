from django.contrib import admin
from .models import Profile,Refferal
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','username')
admin.site.register(Profile,ProfileAdmin)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('id','user','code')
    list_display_links = ('id','user')
admin.site.register(Refferal,ReferralAdmin)