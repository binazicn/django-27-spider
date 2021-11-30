from django.contrib import admin

from .models import spiderdb
# Register your models here.

class SpiderdbAdmin(admin.ModelAdmin):
    list_display = ['crawled','spider','dir_url','url', 'jpg','m3u8','gif']
    list_filter = ['spider']
    search_fields = ['url','crawled']
    list_per_page = 5

admin.site.register(spiderdb,SpiderdbAdmin)
