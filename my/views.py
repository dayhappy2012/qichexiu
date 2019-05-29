import json
import random
import requests
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from my.models import CarUser
from my.serializer import UserSerializer, UserRegisterSerializer, UserLoginSerializer
from utils.error import PramsException


class UserView(viewsets.GenericViewSet, mixins.ListModelMixin):

    queryset = CarUser.objects.all()
    serializer_class = UserSerializer
    
    def list(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        user_id = cache.get(token)
        user = CarUser.objects.filter(id=user_id).first()
        serializer = self.get_serializer(user)

        res = {
            'user_info': serializer.data
        }
        return Response(res)

    @list_route(methods=['POST'], serializer_class=UserRegisterSerializer)
    def register(self, request):
        serializers = self.get_serializer(data=request.data)
        result = serializers.is_valid(raise_exception=True)

        if not result:
            raise PramsException({'code': 1004, 'msg': '注册参数有误'})
        data = serializers.register_data(serializers.data)
        return Response(data)

    @list_route(methods=['POST'], serializer_class=UserLoginSerializer)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        result = serializer.is_valid(raise_exception=True)

        if not result:
            raise PramsException({'code': 1007, 'msg': '参数错误!'})
        res = serializer.login_data(serializer.data)
        return Response(res)

    @list_route(methods=['POST'])
    def send_message_example(self, request):
        number = request.POST.get('phone_number')
        list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        veri_out = random.sample(list_num, 6)
        veri_res = str(veri_out[0]) + str(veri_out[1]) + str(veri_out[2]) + str(veri_out[3]) + str(veri_out[4]) + str(veri_out[5])
        resp = requests.post("http://sms-api.luosimao.com/v1/send.json",
                             auth=("api", "6980fad72b3ec043ef216e067fce9bb7"),
                             data={"mobile": "%s" % number,
                                   "message": "验证码是: %s【铁壳测试】" % veri_res},
                             timeout=3, verify=False)
        res = {'yanzhengma': veri_res, 'result': json.loads(resp.content)}
        return Response(res)



