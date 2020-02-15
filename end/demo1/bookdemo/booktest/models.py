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

class UserManager(models.Manager):
    def deleteByTelePhone(self,tele):
        user=self.get(telephone=tele)
        user.delete()


class User(models.Model):
    telephone = models.CharField(max_length=11,null=True,blank=True)
    objects=UserManager()


    def __str__(self):
        return self.telephone



# 模型类的关联关系


# 一对一   一方Account  实例a   一方Concact 实例c   关系字段定义在任意一方
# a 找 c  a.concact
# c 找 a  c.account

class Account(models.Model):
    username=models.CharField(max_length=20,verbose_name="用户名")
    password=models.CharField(max_length=20,verbose_name="密码")
    regist_date=models.DateField(auto_now_add=True,verbose_name="注册日期")


class Concact(models.Model):
    telephone=models.CharField(max_length=11,verbose_name="手机号")
    email=models.EmailField(default="1335909103@qq.com")
    account=models.OneToOneField(Account,on_delete=models.CASCADE)


# 多对多  多方Article  实例a    多方Tag 实例t   关系字段可以定义在任意一方
# 添加关系   t.articles.add(a)    移除关系  t.articles.remove(a)
# a 找 所有的 t   a.tag_set.all()   如果定义过related_name='tags' 则使用 a.tags.all()
# t 找 所有的 a   t.articles.all()
class Article(models.Model):
    title=models.CharField(max_length=20,verbose_name="标题")
    sumary=models.TextField(verbose_name="正文")

class Tag(models.Model):
    name=models.CharField(max_length=20,verbose_name="标签名")
    articles=models.ManyToManyField(Article)

