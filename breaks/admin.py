from django.contrib import admin
from django.contrib.admin import TabularInline

from .models import organizations, groups, replacements, dicts, breaks


class ReplacementEmployeeInline(TabularInline):
    model = replacements.ReplacementEmployee
    fields = ('employee', 'status',)


@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager',)


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)
    list_display_links = ('code', 'name', 'sort',)


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(replacements.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration',)
    list_display_links = ('group',)
    inlines = (ReplacementEmployeeInline,)


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'replacement', 'break_start', 'break_end', 'status',
    )
