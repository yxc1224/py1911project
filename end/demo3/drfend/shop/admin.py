from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)
admin.site.register(Good)
admin.site.register(GoodImgs)
admin.site.register(User)
admin.site.register(Order)