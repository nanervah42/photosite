from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Avatar, Carousel, InstagramSection, WorksPhotos, WorksCategory


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'is_published', 'get_photo')
    list_editable = ('is_published',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'is_published', 'get_photo')
    list_editable = ('is_published',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'


class InstagramSectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'is_published', 'get_photo')
    list_editable = ('is_published',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'


class WorksCategoryAdmin(admin.ModelAdmin):  # класс редактор
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class WorksPhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo', 'category', 'is_published', 'get_photo')
    list_editable = ('is_published', 'category')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return 'Фото не установлено'

    get_photo.short_description = 'Миниатюра'






admin.site.register(Avatar, AvatarAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(InstagramSection, InstagramSectionAdmin)
admin.site.register(WorksCategory, WorksCategoryAdmin)
admin.site.register(WorksPhotos, WorksPhotosAdmin)

admin.site.site_title = 'Администрирование'
admin.site.site_header = 'Администрирование'