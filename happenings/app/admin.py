from django.contrib import admin
from . import models


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Happening)
class HappeningAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Registration)
class RegistrationAdmin(admin.ModelAdmin):
    pass