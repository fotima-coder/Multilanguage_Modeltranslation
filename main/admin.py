from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post
from django.contrib import admin
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title',)

    # Admin panelda tillarni bir-biriga o'tuvchi Tab (oyna) ko'rinishiga keltirish
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation.css',),
        }