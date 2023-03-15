from django.contrib import admin

from .models import UserAccount, Dustbin, DustbinGroup

admin.site.register(UserAccount)
admin.site.register(Dustbin)
admin.site.register(DustbinGroup)
