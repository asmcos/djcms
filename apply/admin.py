from django.contrib import admin
 
from .models import Events,UserJoin


class EventsAdmin(admin.ModelAdmin):
    list_display =('title',)

class UserJoinAdmin(admin.ModelAdmin):
    list_display =('name','email','company',)

admin.site.register(Events,EventsAdmin)
admin.site.register(UserJoin,UserJoinAdmin)
