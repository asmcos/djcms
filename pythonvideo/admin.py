#coding=utf-8
from django.contrib import admin 
from .models import Category,Course,Video,TextInfo,ImgInfo

class CategoryAdmin(admin.ModelAdmin):
	list_display=('title',)
class CourseAdmin(admin.ModelAdmin):
	list_display=('title',)
	class Media:
               js=("/static/game/js/jquery.min.js","/static/tinymce/js/tinymce/jquery.tinymce.min.js","/static/tinymce/js/tinymce/tinymce.min.js","/static/game/js/tinyedit_intro.js",)

class VideoAdmin(admin.ModelAdmin):
	list_display=('title',)
class TextInfoAdmin(admin.ModelAdmin):
    list_display =('text','tagname',)

class ImgInfoAdmin(admin.ModelAdmin):
    list_display =('image','tagname',)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Video,VideoAdmin)
admin.site.register(TextInfo,TextInfoAdmin)
admin.site.register(ImgInfo,ImgInfoAdmin)
