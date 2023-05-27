from django.contrib import admin
from .models import RD, DB

@admin.register(RD)
class RDAdmin(admin.ModelAdmin):
    pass

@admin.register(DB)
class DBAdmin(admin.ModelAdmin):
    pass
