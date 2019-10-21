from django.contrib import admin
from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Happening)
class HappeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date')
    

@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'happening')
    list_filter = ['happening']