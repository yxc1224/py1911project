from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse

# django自带分页和分页器
from django.core.paginator import Paginator, Page

# 一个Page中有  object_list 代表当前页的所有对象
# has_next  是不是有下一页
# has_previous  是不是有上一页
# next_page_number  下一页的编号
#  previous_page_number 上一页的编号
# self。number  当前页的编号
# self.paginator  当前页的分页器

#  一个Paginator中的 object_list 代表所有未分页对象
# self.per_page 每一页有几个对象
# get_page(self, number)  从分页器中取第几页
# page_range(self)  返回分页列表


from .models import *
from .forms import *


# Create your views here.

def index(request):
    ads = Ads.objects.all()
    typepage = request.GET.get("type")
    year = None
    month = None
    category_id = None
    tag_id = None
    if typepage == "date":
        year = request.GET.get("year")
        month = request.GET.get("month")
        articles = Article.objects.filter(create_time__year=year, create_time__month=month)
    elif typepage == "category":
        category_id = request.GET.get("category_id")
        category = Category.objects.get(id=category_id, )
        articles = category.article_set.all()
    elif typepage == "tag":
        tag_id = request.GET.get("tag_id")
        tag = Tag.objects.get(id=tag_id)
        articles = tag.article_set.all()
    else:
        # locals() 可以返回作用域局部变量
        articles = Article.objects.all()
    paginator = Paginator(articles, 2)
    num = request.GET.get("pagenum", 1)
    page = paginator.get_page(num)

    return render(request, 'index.html', {"ads": ads, "page": page, "typepage": typepage, "year": year, "month": month,
                                          "category_id": category_id, "tag_id": tag_id})
    # return render(request,locals())


def detail(request, articleid):
    if request.method == "GET":

        article = Article.objects.get(id=articleid)
        cf = CommentForm()
        return render(request, 'single.html', locals())
    elif request.method == "POST":
        cf = CommentForm(request.POST)
        if cf.is_valid():
            comment=cf.save(commit=False)
            comment.article = Article.objects.get(id=articleid)
            comment.save()
            url = reverse("blogapp:detail", args=(articleid,))
            return redirect(to=url)
        else:
            article = Article.objects.get(id=articleid)
            cf = CommentForm()
            errors = "信息有误"
            return render(request, 'single.html', locals())


def contact(request):
    return render(request, 'contact.html')


def favicon(request):
    return redirect(to="/static/favicon.ico")
