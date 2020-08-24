from django.contrib import admin
from .models import User, UserVar, Group, Context, ContextAction, IVR, IVREntry


class UserVarInline(admin.TabularInline):
    model = UserVar
    show_change_link = True
    extra = 0


class ContextActionInline(admin.TabularInline):
    model = ContextAction
    fields = ['prio', 'condition_field', 'condition_value', 'action', 'action_value']
    show_change_link = True
    extra = 0
    ordering = ['prio']


class IVREntryInline(admin.TabularInline):
    model = IVREntry
    fields = ['action', 'digit', 'param']
    show_change_link = True
    extra = 0


@admin.register(IVR)
class IVRAdmin(admin.ModelAdmin):
    fields = ('name', 'greet_long', 'greet_short', 'invalid_sound', 'exit_sound', 'timeout', 'max_failures')
    list_display = ('name', 'timeout', 'max_failures')
    search_fields = ["name",]
    inlines = [IVREntryInline,]


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ('number', 'password')
    list_display = ('number', 'password')
    search_fields = ["number"]
    inlines = [UserVarInline,]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    fields = ('name', 'members')
    autocomplete_fields = ('members',)


@admin.register(Context)
class ContextAdmin(admin.ModelAdmin):
    fields = ('name',)
    inlines = [ContextActionInline,]