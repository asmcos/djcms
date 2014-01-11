from django.contrib import admin
 
from .models import TextInfo,ImgInfo,StudentsApp

class TextInfoAdmin(admin.ModelAdmin):
    list_display =('text','tagname',)

class ImgInfoAdmin(admin.ModelAdmin):
    list_display =('image','tagname',)

class StudentsAppAdmin(admin.ModelAdmin):
    list_display =('title1',)

admin.site.register(TextInfo,TextInfoAdmin)
admin.site.register(ImgInfo,ImgInfoAdmin)
admin.site.register(StudentsApp,StudentsAppAdmin)
