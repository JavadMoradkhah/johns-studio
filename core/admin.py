from django.contrib import admin
from . import models

admin.site.site_header = 'John\'s Studio Administration'
admin.site.site_title = 'John\'s Studio Administration'
admin.site.index_title = 'John\'s Studio Administration'

LIST_PER_PAGE = 10


class ProfileInline(admin.StackedInline):
    model = models.Profile


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name',
                    'is_staff', 'is_active', 'is_superuser')
    inlines = (ProfileInline,)
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'date_joined')
    LIST_PER_PAGE = LIST_PER_PAGE


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    LIST_PER_PAGE = LIST_PER_PAGE


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {
        'slug': ['name']
    }
    search_fields = ('name', 'slug')
    ordering = ('name',)
    LIST_PER_PAGE = LIST_PER_PAGE


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('caption', 'category', 'created', 'updated')
    search_fields = ('caption',)
    autocomplete_fields = ('category',)
    list_filter = ('category', 'created')
    LIST_PER_PAGE = LIST_PER_PAGE


@admin.register(models.InstagramPost)
class InstagramPostAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'link', 'created')
    list_select_related = ('portfolio',)
    autocomplete_fields = ('portfolio',)
    LIST_PER_PAGE = LIST_PER_PAGE


@admin.register(models.Slide)
class SlideAdmin(admin.ModelAdmin):
    list_display = ('portfolio', 'text', 'created')
    autocomplete_fields = ('portfolio',)
    LIST_PER_PAGE = LIST_PER_PAGE


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created')
    LIST_PER_PAGE = LIST_PER_PAGE


@admin.register(models.ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    LIST_PER_PAGE = 1


@admin.register(models.SocialMediaInfo)
class SocialMediaInfoAdmin(admin.ModelAdmin):
    LIST_PER_PAGE = 1
