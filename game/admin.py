from django.contrib import admin
 
from .models import TextInfo,ImgInfo,StudentsApp,Teacher,Singlepage


class TextInfoAdmin(admin.ModelAdmin):
    list_display =('text','tagname',)
    class Media:
	js=("/static/game/js/jquery.min.js","/static/tinymce/js/tinymce/jquery.tinymce.min.js","/static/tinymce/js/tinymce/tinymce.min.js","/static/game/js/tinyedit.js",)

class ImgInfoAdmin(admin.ModelAdmin):
    list_display =('image_tag','tagname',)

class StudentsAppAdmin(admin.ModelAdmin):
    list_display =('title1',)

class TeacherAdmin(admin.ModelAdmin):
    list_display =('name',)

class SinglepageAdmin(admin.ModelAdmin):
    list_display =('title',)
    class Media:
	js=("/static/game/js/jquery.min.js","/static/tinymce/js/tinymce/jquery.tinymce.min.js","/static/tinymce/js/tinymce/tinymce.min.js","/static/game/js/tinyedit.js",)
admin.site.register(TextInfo,TextInfoAdmin)
admin.site.register(ImgInfo,ImgInfoAdmin)
admin.site.register(StudentsApp,StudentsAppAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(Singlepage,SinglepageAdmin)
