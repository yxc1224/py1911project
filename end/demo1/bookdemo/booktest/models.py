from django.db import models


# Create your models here.
# 有了模型类之后模型类如何与数据库交互
# 1注册模型 在setting.py 中的INSTALLED_APPS 添加应用名
# 2生成迁移文件  用于与数据库交互 python manage.py makemigrations
# 3执行迁移 会在对应的数据库中生成对应的表  python manage.py migrate
class Book(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField(default="1983-06-01")
    price=models.FloatField(default=0)

    def __str__(self):
        return self.title

class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=(('male', '男'), ('female', '女')))
    content = models.CharField(max_length=100)

    # book  是一对多中的外键  on_delete代表删除主表数据是如何做响应
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name