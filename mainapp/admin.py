from django.contrib import admin
from .models import Region, Position, Degree, Family, ComputerScience, Application


admin.site.register(Region)
admin.site.register(Position)
admin.site.register(Degree)
admin.site.register(Family)
admin.site.register(ComputerScience)


@admin.register(Application)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number', 'degree', 'region', 'family', 'position']
    list_filter = ['degree__name', 'region__name', 'computer_science__name', 'family__name', 'degree__name', 'position__name']
    search_fileds = ['first_name', 'last_name', 'degree__name', 'region__name', 'computer_science__name', 'family__name', 'degree__name', 'position__name']
    ordering = ['-date_time']
