from django.contrib import admin
from . import models

@admin.register(models.Member)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'account_id',
        'email',
        'nickname',
        'phone_number',
        'name',
    )

    list_display_links = (
        'nickname',
        'email',
    )