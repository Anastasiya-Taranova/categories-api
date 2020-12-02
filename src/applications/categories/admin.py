from django.contrib import admin

from applications.categories.models import Category


@admin.register(Category)
class CategoryAdminModel(admin.ModelAdmin):
    pass
