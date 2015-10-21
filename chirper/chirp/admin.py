from django.contrib import admin
from chirp.models import Chirp


@admin.register(Chirp)
class ChirpAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'posted_at')