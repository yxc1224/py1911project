from django import  forms
from .models import User

class LoginForm(forms.Form):
    """
    定义一个登录表单  用于生成html登录表单
    """
    username = forms.CharField(max_length=15,min_length=3,label="输入用户名",help_text="最少3，最大15")
    password = forms.CharField(max_length=15,min_length=3,widget=forms.PasswordInput,help_text="最少3，最大15")
