from rest_framework import serializers
from .models import *


class GoodSerializer1(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Good
        fields = "__all__"


class CustomSerializer(serializers.RelatedField):
    """
    自定义一序列化类
    """

    def to_representation(self, value):
        return str(value.id) + '--' + value.name + '--' + value.desc


class CategorySerializer(serializers.Serializer):
    """
    序列化类  决定了模型序列化细节
    """
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    # 重写创建方法
    def create(self, validated_data):
        # print(validated_data)
        instance = Category.objects.create(**validated_data)
        return instance

    #  重写更新方法
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.save()
        return instance


class CategorySerializer1(serializers.ModelSerializer):
    """
    编写针对category的序列号类
    本类指明了cate的序列化细节
    需要继承ModelSerializer  才可以针对模型进行序列化

    """
    # goods一定要和related_name的值一样  many=True 代表多个对象  read_only=True 代表只读
    # goods = serializers.StringRelatedField(many=True)

    # PrimaryKeyRelatedField 只显示主键
    # goods = serializers.PrimaryKeyRelatedField(many=True,read_only=True)

    # SlugRelatedField  显示自定义字段
    goods = serializers.SlugRelatedField(slug_field='name', many=True, read_only=True)

    # 显示资源RestFulAPI
    # goods = serializers.HyperlinkedRelatedField(read_only=True,many=True,view_name='good-detail')

    # goods =CustomSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        fields = ('id', 'name', 'goods')


class GoodImgsSerializer(serializers.Serializer):
    img = serializers.ImageField()
    good = serializers.CharField(source='good.name')

    def validate(self, attrs):
        try:
            g = Good.objects.get(name=attrs["good"]["name"])
            attrs["good"] = g
            return attrs
        except:
            raise serializers.ValidationError("输入的商品不存在")

    def create(self, validated_data):
        instance = GoodImgs.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.img = validated_data.get("img", instance.img)
        instance.good = validated_data.get("good", instance.good)
        instance.save()
        return instance


class GoodSerializer(serializers.Serializer):
    name = serializers.CharField()
    category = CategorySerializer()
    imgs = GoodImgsSerializer(label="图片", many=True, read_only=True)

    def validate_category(self, category):
        """
        处理category
        :param category: 处理的原始值
        :return: 返回的新值
        """
        print("category的原始值为", category)
        try:
            Category.objects.get(name=category['name'])
        except:
            raise serializers.ValidationError("输入的分类不存在")
        return category

    def validate(self, attrs):

        c = Category.objects.get(name=attrs["category"]["name"])
        attrs["category"] = c
        return attrs

    def create(self, validated_data):
        instance = Good.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.category = validated_data.get("category", instance.category)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserRegistSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=10, min_length=3)
    password = serializers.CharField(max_length=10, min_length=3,write_only=True)
    password2 = serializers.CharField(max_length=10, min_length=3,write_only=True)

    def validate_password2(self, data):
        if data != self.initial_data["password"]:
            raise serializers.ValidationError("密码不一致")
        else:
            return data

    def create(self, validated_data):
        return User.objects.create_user(username=validated_data.get('username'), email=validated_data.get('email'),
                                        password=validated_data.get('password'))
