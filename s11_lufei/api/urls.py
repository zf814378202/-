from django.conf.urls import url
from api.views import course,shoppingcar

urlpatterns = [
    url(r'coursesview/$', course.CoursesView.as_view({'get': 'list'})),
    url(r'degreecourseview/$', course.DegreeCourseView.as_view),
    url(r'courses/(?P<pk>\d+)/$', course.CourseDetailView.as_view),
    url(r'questionview/(?P<pk>\d+)/$', course.QuestionView.as_view),
    url(r'outlineview/(?P<pk>\d+)/$', course.OutlineView.as_view),
    url(r'chapterview/(?P<pk>\d+)/$', course.ChapterView.as_view),

    url(r'shoppingcar/$', shoppingcar.ShoppingCarView.as_view({'post':'create','get':'list'})),


 ]
