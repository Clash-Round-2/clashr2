from django.conf.urls import url
from basic_app import views


app_name = 'basic_app'


urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^questions/$',views.question_panel,name='question_panel'),
    url(r'codingpage/(?P<id>\d+)/$',views.questions,name='questions'),
    url(r'codingpage/$',views.questions,name='questions'),
    url(r'leader/$',views.leader,name='leader'),


]
