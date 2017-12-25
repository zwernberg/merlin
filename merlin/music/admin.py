from django.contrib import admin
from adminsortable.admin import SortableAdmin
from merlin.music.models import Song, Category

# Register your models here.

class SongAdmin(SortableAdmin):
    list_display = ['__str__', 'artist', 'category', 'fan_votes']


admin.site.register(Category, SortableAdmin)
admin.site.register(Song, SongAdmin)
