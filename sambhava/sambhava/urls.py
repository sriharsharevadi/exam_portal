"""sambhava URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from webapp import views

router = routers.DefaultRouter()
router.register(r'users', views.BaseUserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'institutes', views.InstituteViewSet, basename='institutes')
router.register(r'students', views.StudentViewSet, basename='students')
router.register(r'batches', views.BatchViewSet, basename='batches')
router.register(r'papers', views.PaperViewSet, basename='papers')
router.register(r'exams', views.ExamViewSet, basename='exams')
router.register(r'questions', views.QuestionViewSet, basename='questions')
router.register(r'results', views.ResultViewSet, basename='results')
router.register(r'attempted_questions', views.AttemptedQuestionViewSet, basename='attempted_questions')
# router.register(r'student_list', views.StudentList, basename='student')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('student/<int:institute_id>/', views.StudentList.as_view()),


]
