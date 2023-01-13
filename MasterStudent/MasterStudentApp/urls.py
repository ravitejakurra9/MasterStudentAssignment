from django.urls import path

from MasterStudentApp import views

urlpatterns=[
    path('',views.index_fun),
    path('masterlog',views.masterlog_fun,name='mlog'),
    path('masterreg',views.masterreg_fun,name='mreg'),
    path('studentlog',views.studentlog_fun,name='slog'),
    path('studentreg',views.studentreg_fun,name='sreg'),
    path('a_task',views.a_task_fun,name='a_task'),
    path('taskdata',views.taskdata_fun),
    path('solve/<int:id>',views.slove_fun,name='sol'),
    path('stddata',views.stddata_fun,name='stddata'),
    path('alltask',views.viewalltask_fun,name='alltask'),
    path('master_home',views.m_home_fun,name='m_home')

]