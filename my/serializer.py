import uuid

from django.contrib.auth.hashers import make_password, check_password
from django.core.cache import cache
from rest_framework import serializers

from my.models import CarUser
from utils.error import PramsException


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarUser
        fields = "__all__"


class UserRegisterSerializer(serializers.Serializer):
    c_username = serializers.CharField(required=True, max_length=16, min_length=1,
                                       error_messages={'required': '注册账号必填',
                                                       'max_length': '注册账号不能超多16位',
                                                       'min_length': '注册账号不能低于1位'})

    c_phone = serializers.CharField(required=True, max_length=12, min_length=10,
                                    error_messages={'required': '注册账号必填',
                                                    'max_length': '注册账号是１１位',
                                                    'min_length': '注册账号是１１位'})

    c_password = serializers.CharField(required=True, max_length=16, min_length=1,
                                       error_messages={'required': '密码必填',
                                                       'max_length': '注册密码不能超多16位',
                                                       'min_length': '注册密码不能低于1位'})
    c_password2 = serializers.CharField(required=True, max_length=16, min_length=1,
                                       error_messages={'required': '密码必填',
                                                       'max_length': '注册密码不能超多16位',
                                                       'min_length': '注册密码不能低于1位'})

    def validate(self, attrs):
        username = attrs.get('c_username')
        if CarUser.objects.filter(c_username=username).exists():
            raise PramsException({'code': 1001, 'msg': '账号已存在'})
        if attrs.get('u_password') != attrs.get('u_password2'):
            raise PramsException({'code': 1002, 'msg': '密码不一致,注册失败'})
        return attrs

    def register_data(self, validate_data):
        c_password = make_password(validate_data['c_password'])
        CarUser.objects.create(c_username=validate_data['c_username'],
                               c_password=c_password,
                               c_phone=validate_data['c_phone'])
        res = {
            'code': 200,
            'msg': '注册成功'}
        return res


class UserLoginSerializer(serializers.Serializer):
    c_username = serializers.CharField(required=True, max_length=32, min_length=1,
                                       error_messages={'required': '账号必填',
                                                       'max_length': '账号不能超多32位',
                                                       'min_length': '账号不能低于4位'})
    c_password = serializers.CharField(required=True, max_length=10, min_length=1,
                                       error_messages={'required': '密码必填',
                                                       'max_length': '密码不能超多10位',
                                                       'min_length': '密码不能低于4位'})

    def validate(self, attrs):
        if not CarUser.objects.filter(c_username=attrs.get('c_username')).exists():
            raise PramsException({'code': 1005, 'msg': '账号不存在'})

        user = CarUser.objects.filter(c_username=attrs.get('c_username')).first()
        if not check_password(attrs.get('c_password'), user.c_password):
            raise PramsException({'code': 1006, 'msg': '密码错误！'})
        return attrs

    def login_data(self, validate_data):
        token = uuid.uuid4().hex
        user = CarUser.objects.filter(c_username=validate_data['c_username']).first()
        cache.set(token, user.id, timeout=60 * 60 * 7)
        res = {'token': token}
        return res

