
from rest_framework import serializers
from api import models
# a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseSerializer(serializers.Serializer):
    name = serializers.CharField()
    teachers = serializers.SerializerMethodField()
    class Meta:
        model = models.DegreeCourse
        fields = ['id','name','teachers']
    def get_teachers(self,obj):
        teachers_list = obj.teachers.all()
        return  [ {'name':item.name} for item in teachers_list]


# c.展示所有的专题课
class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
# d. 查看id=1的学位课对应的所有模块名称

# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class QuestionSerializer(serializers.Serializer):
    ask = serializers.SerializerMethodField()
    def get_ask(self,obj):
        ask_list = obj.asked_question.all()
        return [[(item.question,item.answer) for item in ask_list]]
    class Meta:
        model = models.Course
        fields = ['ask']
 # g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseOutlineSerializer(serializers.Serializer):
     outline = serializers.SerializerMethodField()
     def get_outline(self,obj):
         outline_list = obj.coursedetail.courseoutline_set.all()
         return [(item.title,item.content) for item in outline_list]
     class Meta:
         model = models.Course
         fields = ['outline']


# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CourseChapterSerializer(serializers.Serializer):
    chapter = serializers.CharField()
    class Meta:
        models = models.Course
        fields = ['chapter']