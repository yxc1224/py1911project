from django.contrib import admin
from  django.contrib.admin import ModelAdmin

# Register your models here.
from .models import User,Pollsmsg,Polls

class PollsmgsInline(admin.StackedInline):
    model = Pollsmsg
    extra = 1


class PollsmsgAdmin(ModelAdmin):
    list_display = ("msg","coutmsg","polls")
    search_fields=("msg",)

class PollsAdmin(ModelAdmin):
    list_display = ("polls_text",)
    search_fields = ('polls_text',)
    inlines = [PollsmgsInline]

admin.site.register(Polls,PollsAdmin)
admin.site.register(Pollsmsg,PollsmsgAdmin)
admin.site.register(User)

