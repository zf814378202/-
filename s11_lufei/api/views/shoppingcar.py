import json
import  redis
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.parsers import JSONParser,FormParser
from  api import models
from api.utils.response import BaseResponse

CONN = redis.Redis(host='192.168.11.146',port=6379)

USER_ID = 5

class ShoppingCarView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        '''
        查看购物车的信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        response = BaseResponse()
        try:
            shopping_car_course_list = []   #创建一个科目列表
            pattern = settings.LUFFY_SHOPPING_CAR %(USER_ID,'*') #查找USER ID并替换为查找出来的ID

            user_key_list = CONN.keys(pattern)
            for key in user_key_list:
                '''
                创建购物车数据格式
                课程ID
                课程名称
                课程图片
                默认选中的价格策略id
                所有价格策略id
                
                '''
                temp = {
                    'id': CONN.hget(key, 'id').decode('utf-8'),
                    'name': CONN.hget(key, 'name').decode('utf-8'),
                    'img': CONN.hget(key, 'img').decode('utf-8'),
                    'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                    'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
                }
                shopping_car_course_list.append(temp)
                response.data = shopping_car_course_list

        except Exception as e:
            response.code = 10000
            response.error = '获取购物车失败'
        return Response(response.dict)

    def create(self,request,*args,**kwargs):
        '''
        将商品加入购物车

        1.接收用户选中的课程ID和价格策略ID
        2.要判断用户的合法性
            -课程是否存在
            -价格策略是否合法
        3.把商品信息和价格策略放入购物车中

        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 1.接收用户选中的课程id和价格id
        course_id = request.data.get('courseid')
        policy_id = request.data.get('policyid')
        print(policy_id )
        #2.判断用户的合法性
            # -课程是否存在
            # -价格策略是否合法


        #判断课程是否存在
        course = models.Course.objects.filter(id=course_id).first()
        if not course:
            return Response({'code':101,'error':'课程不存在'})

        #价格是否合法
        price_policy_queryset = course.price_policy.all()
        price_policy_dict = {}
        for item in price_policy_queryset:
            temp = {

                'id':item.id,
                'price':item.price,
                'valid_period':item.valid_period,#取出所有的价格策略
                'valid_period_display':item.get_valid_period_display()

            }


            price_policy_dict[item.id] = temp
            print('******',temp)


        if policy_id not in price_policy_dict:
            return Response({'code':102,'error':'价格策略错误'})
        #限制购物车物品数量
        pattern = settings.LUFFY_SHOPPING_CAR %(USER_ID,'*')
        keys = CONN.keys(pattern)
        if keys and len(keys) >= 100:
            return Response({'code':'1008','error':'购物车已满请清空购物车'})

        key = settings.LUFFY_SHOPPING_CAR % (USER_ID, course_id,)
        CONN.hset(key, 'id', course_id)
        CONN.hset(key, 'name', course.name)
        CONN.hset(key, 'img', course.course_img)
        CONN.hset(key, 'default_price_id', policy_id)
        CONN.hset(key, 'price_policy_dict', json.dumps(price_policy_dict))
        #限制购物车的中物品的保留时间
        CONN.expire(key, 20 * 60)


        return Response({'code': 10000, 'data': '购买成功'})



    def destroy(self,request,*args,**kwargs):
        '''
        删除购物车中的物品
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        response = BaseResponse()
        try:
            courseid = request.GET.get('courseid')

            key = settings.LUFFY_SHOPPING_CAR %(USER_ID,courseid,)

            CONN.delete(key)
            request.datd = '删除成功'

        except Exception as e:
            response.code = 104
            response.error = '删除失败'

        return Response(response.dict)

    def update(self,request,*args,**kwargs):
        '''
        修改用户的价格策略

            获取课程ID 和要修改的策略ID
            2.去redis中效验合法性
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        response = BaseResponse()
        try:
            #获取 获取课程ID 和要修改的策略ID
            course_id = request.data.get('courseid')
            policy_id = request.data.get('policyid') if request.data.get('policyid') else None


            key = settings.LUFFY_SHOPPING_CAR %(USER_ID,course_id,)

            #去redis中效验合法性
            if not CONN.exists(key):
                response.code = 105
                response.error = '课程不存在'
                return  Response(response.dict)
            price_policy_dict = json.loads(CONN.hget(key,'price_policy_dict').decode('utf-8'))

            if policy_id not  in price_policy_dict:
                response.code = 106
                response.error = '价格策略不存在'

                return  Response(response.dict)
            CONN.hset(key,'default_price_id',policy_id)
            CONN.expire(key,20*60)
            response.data = '修改成功'
        except Exception as e:
            response.code = 1004
            response.error = '错误'

        return  Response(response.dict)

