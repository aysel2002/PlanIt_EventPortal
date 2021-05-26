from django.contrib import admin
from .models import User, Admin, Event, Book_ground,upcoming_events

# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Event)
admin.site.register(Book_ground)
admin.site.register(upcoming_events)
