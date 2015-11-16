from django.contrib import admin
from chirp.models import Chirp, Tag


@admin.register(Chirp)
class ChirpAdmin(admin.ModelAdmin):
    list_display = ('author', 'message', 'posted_at')
    list_filter = ('author', 'posted_at')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'posted_at')