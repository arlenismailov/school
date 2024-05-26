from django.contrib import admin
from .models import *

admin.site.register(UserProfile)
admin.site.register(Teacher)
admin.site.register(Relation)


class PhotoEventsInline(admin.TabularInline):
    model = PhotoEvents
    extra = 1


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    inlines = [PhotoEventsInline]