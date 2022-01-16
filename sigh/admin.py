from django.contrib import admin
from sigh.models import SighModel

@admin.register(SighModel)
class Sighmodel(admin.ModelAdmin):
    pass