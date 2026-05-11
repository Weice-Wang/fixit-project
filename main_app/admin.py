from django.contrib import admin
from .models import Item, Maintaining, Tag

admin.site.register(Item)
admin.site.register(Maintaining)
admin.site.register(Tag)