from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all-groups/$', views.allGroups, name="allGroups"),
    url(r'^(?P<group_id>[0-9]+)/get-group/$', views.groupById, name="groupById"),
    url(r'^(?P<question_id>[0-9]+)/get-question/$', views.questionById, name="questionById"),
    url(r'^make-group', views.makeGroup, name='MakeGroup'),
    url(r'^make-question', views.makeQuestion, name='MakeQuestion')
]