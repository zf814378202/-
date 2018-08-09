from django.shortcuts import render, HttpResponse
from api import models
from django.views import View

# Create your views here.
# 作业：
# 一、准备工作：
# 1.
# 通过admin对13张表录入数据
# 2.
# ORM练习
class Index(View):
    def index(request):
        # a.查看所有学位课并打印学位课名称以及授课老师

        # obj = models.DegreeCourse.objects.all().values('name','teachers__name')

        # obj = models.DegreeCourse.objects.all()
        # for i in obj:

        # b.查看所有学位课并打印学位课名称以及学位课的奖学金
        #   obj = models.DegreeCourse.objects.all().values('name','total_scholarship')
        #     obj = models.DegreeCourse.objects.all()
        #     for i in obj:
        #         print(i.name)
        #         ships = i.scholarship_set.all()
        #         for item in ships:
        #             print('=========',item.time_percent,item.value)
        # c.展示所有的专题课
        #     obj = models.Course.objects.filter(degree_course__isnull=True)
        #        print(boj)

        # d.查看id = 1的学位课对应的所有模块名
        # obj = models.DegreeCourse.objects.filter(id=5).values('name')
        #     obj = models.Course.objects.filter(degree_course_id=7)
        #     obj = models.DegreeCourse.objects.get(id=5)
        #     course_list = obj.course_set.all()
        #     print(course_list)
        #     course_list = models.Course.objects.filter(degree_course_id=5)
        #     print(course_list)

        # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
        #     obj = models.Course.objects.filter(id=5).values('name','')
        # obj = models.Course.objects.get(id=5)
        # print(obj.name)
        # print(obj.brief)
        # print(obj.get_level_display())
        # print(obj.coursedetail.hours)
        # print(obj.coursedetail.why_study)
        # print(obj.coursedetail.recommend_courses.all())

        # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
        #     obj = models.OftenAskedQuestion.objects.filter(object_id=5,content_type__model='course').values('question')
        # obj = models.Course.objects.get(id=5)
        # ask_list = obj.asked_question.all()
        # for item in ask_list:
        #     print(item.question, item.answer)


        # g.获取id = 1 的专题课，并打印该课程相关的课程大纲
        #     obj = models.Course.objects.filter(id=6).values('coursedetail__courseoutline__title')
        # obj = models.Course.objects.get(id=5)
        # obj_list = obj.coursedetail.courseoutline_set.all()
        # for item in obj_list:
        #     print(item.title,item.content)

        #
        # h.获取id = 1的专题课，并打印该课程相关的所有章节
        #     obj = models.Course.objects.filter(id=5).values('coursechapters__chapter','coursechapters__name')
        #
        # obj = models.Course.objects.get(id=5)
        # chap_list = obj.coursechapters.all()
        # for item in chap_list:
        #     print(item.name)
        # # i.获取id = 1的专题课，并打印该课程相关的所有课时
        # #     obj = models.Course.objects.filter(id=5).values('coursedetail__hours','coursechapters__coursesections__name')
        #
        # obj = models.Course.objects.get(id=5)
        # chapter_list = obj.coursechapters.all()
        # for chapter in chapter_list:
        #     print(chapter.name,chapter.coursesections.all())
        # # 第1章·Python
        # 介绍、基础语法、流程控制
        #
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 第1章·Python
        # 介绍、基础语法、流程控制
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # 01 - 课程介绍（一）
        # i.获取id = 1的专题课，并打印该课程相关的所有的价格策略
        #     obj = models.PricePolicy.objects.filter(object_id='5',content_type__model='course')

        return HttpResponse('ok')
# 二、基于django
# # rest
# framework
# 写路飞的接口（作业一 + rest
# framework
# 序列化）
# - 课程列表API
# - 课程详细API
