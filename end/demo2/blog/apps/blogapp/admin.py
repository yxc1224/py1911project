from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Ads)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Comment)
