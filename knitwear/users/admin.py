from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday', 'is_staff')
    list_display_links = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_editable = ('is_staff',)
    list_filter = ('is_staff',)


admin.site.register(User)
