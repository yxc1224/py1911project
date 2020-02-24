from django.template import Library
from ..models import Article,Category,Tag

register = Library()

@register.filter
def dateFormat(date):
    return "%d-%d-%d"%(date.year,date.month,date.day)

@register.filter
def authorFormat(author,info):
    return info+":"+author.upper()

@register.simple_tag
def get_latestarticles(num=3):
    return Article.objects.all().order_by("-create_time")


@register.simple_tag
def get_latesdates(num=3):
    dates = Article.objects.dates("create_time","month","DESC")[:num]
    return dates

@register.simple_tag
def get_categorys(num=3):
    return Category.objects.all()[:num]


@register.simple_tag
def gettags():
    return Tag.objects.all()