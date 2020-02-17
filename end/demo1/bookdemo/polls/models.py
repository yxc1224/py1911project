from django.db import models

# Create your models here.


class Polls(models.Model):
    polls_text=models.CharField(max_length=20)
    def __str__(self):
        return self.polls_text

class  Pollsmsg(models.Model):
    msg=models.CharField(max_length=20,verbose_name="内容")
    coutmsg=models.PositiveIntegerField(max_length=10,verbose_name="数量",default=0)

    polls=models.ForeignKey(Polls,on_delete=models.CASCADE)

    def __str__(self):
        return self.msg
