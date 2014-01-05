from django.contrib import admin
 
from .models import TextInfo,ImgInfo

class TextInfoAdmin(admin.ModelAdmin):
    list_display =('text','tagname',)

class ImgInfoAdmin(admin.ModelAdmin):
    list_display =('image','tagname',)
admin.site.register(TextInfo,TextInfoAdmin)
admin.site.register(ImgInfo,ImgInfoAdmin)
