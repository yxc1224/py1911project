from rest_framework import serializers
from .models import *


class CategorySerizlizer(serializers.ModelSerializer):
    """
    编写针对category的序列号类
    本类指明了cate的序列化细节
    需要继承ModelSerializer  才可以针对模型进行序列化

    """
    # goods一定要和related_name的值一样  many=True 代表多个对象
    goods = serializers.StringRelatedField(many=True)
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ('name','goods')

class GoodSerizlizer(serializers.ModelSerializer):

    # 在序列化时指定字段
    class Meta:
        model = Good
        fields = "__all__"