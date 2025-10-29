from django.contrib import admin

from .models import Menu, MenuItem


class MenuItemInline(admin.TabularInline):
    model = MenuItem
    extra = 1
    fk_name = "menu"
    fields = ("title", "parent", "url")


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [MenuItemInline]


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("menu", "title", "parent", "url", "named_url")
    search_fields = ("title",)
    list_filter = ("menu__name", "parent", "named_url")
