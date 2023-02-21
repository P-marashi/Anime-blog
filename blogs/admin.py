from django.contrib import admin
from .models import Article, IPAddress

admin.site.site_header = 'Anime-blog'


# Register your models here.
def make_publish(modeladmin, request, queryset):
    query_updated = queryset.update(status="p")
    if query_updated == 1:
        message_bit = "منتشر شد"
    else:
        message_bit = " منتشر شدند "

    modeladmin.message_user(request, " {} مقاله {} ".format(query_updated, message_bit))


make_publish.short_description = " منتشر کردن مقاله های انتخاب شده"


def make_draft(modeladmin, request, queryset):
    query_updated = queryset.update(status="d")
    if query_updated == 1:
        message_bit = "پیش نویس شد"
    else:
        message_bit = " پیش نویس شدند "

    modeladmin.message_user(request, " {} مقاله {} ".format(query_updated, message_bit))


make_draft.short_description = " پیش نویس کردن مقاله های انتخاب شده"


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'jpublish', 'status', 'thumb_get', 've_thumbnail')
    list_filter = ('publish', 'status', 'update')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', '-publish')
    actions = [make_draft, make_publish]


admin.site.register(Article, ArticleAdmin, )

admin.site.register(IPAddress, )
