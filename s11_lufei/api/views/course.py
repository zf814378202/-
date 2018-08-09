import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination

from api import models
from api.serializers.course import DegreeCourseSerializer,CourseSerializer,CourseOutlineSerializer,QuestionSerializer,CourseChapterSerializer
from api.utils.response import BaseResponse
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet,ModelViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,ListModelMixin
from rest_framework.renderers import JSONRenderer
# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseView(APIView):
    def get(self, request, *args, **kwargs):
        ret = BaseResponse()
        try:
            queryset = models.DegreeCourse.objects.all()
            ser = DegreeCourseSerializer(instance=queryset ,many = True)
            ret.data = ser.data
        except Exception as e:
            ret.code = 500

            ret.error = '获取失败'
        return Response(ret.__dict__)
# b.查看所有学位课并打印学位课名称以及学位课的奖学金


# c.展示所有的专题课
class CoursesView(ListModelMixin,GenericViewSet):
    queryset = models.Course.objects.all()

    def list(self, request, *args, **kwargs):
        course_list = models.Course.objects.all()
        ser = CourseSerializer(instance=course_list, many=True)
        return Response(ser.data)


# d. 查看id=1的学位课对应的所有模块名称
class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.filter(id=pk)
            ser = CourseSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)
# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses



# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class QuestionView(APIView):
    def get(self, request,pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            queryset = models.Course.objects.filter(id=pk)
            ser = QuestionSerializer(instance=queryset ,many = True)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)
# g.获取id = 1的专题课，并打印该课程相关的课程大纲
class OutlineView(APIView):
    def get(self, request,pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            queryset = models.Course.objects.filter(id=pk)
            ser = CourseOutlineSerializer(instance=queryset ,many = True)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)

# h.获取id = 1的专题课，并打印该课程相关的所有章节
class ChapterView(APIView):
    def get(self, request,pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            queryset = models.Course.objects.filter(id=pk)
            ser = CourseChapterSerializer(instance=queryset ,many = True)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)