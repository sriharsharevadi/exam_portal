from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status, viewsets, permissions, filters, mixins
from .models import BaseUser, Institute, Student, Batch, Paper, Section, Exam, Question, Result, AttemptedQuestion
from django.contrib.auth.models import Group
from .serializers import InstituteSerializer, BaseUserSerializer, GroupSerializer, StudentSerializer, BatchSerializer, PaperSerializer, SectionSerializer,ExamSerializer, QuestionSerializer, ResultSerializer, AttemptedQuestionSerializer

# Create your views here.


class BaseUserViewSet(viewsets.ModelViewSet):
    queryset = BaseUser.objects.all().order_by('-date_joined')
    serializer_class = BaseUserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self):
        queryset = Student.objects.all()
        institute = self.request.query_params.get('institute', None)
        if institute is not None and self.action == 'list':
            institute = institute.title()
            queryset = queryset.filter(institute_id=institute)
        return queryset

    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
    permission_classes = [permissions.IsAuthenticated]


class BatchViewSet(viewsets.ModelViewSet):
    serializer_class = BatchSerializer

    def get_queryset(self):
        queryset = Batch.objects.all()
        institute = self.request.query_params.get('institute', None)
        if institute is not None and self.action == 'list':
            institute = institute.title()
            queryset = queryset.filter(institute_id=institute)
        return queryset

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]


class PaperViewSet(viewsets.ModelViewSet):
    serializer_class = PaperSerializer

    def get_queryset(self):
        queryset = Paper.objects.all()
        institute = self.request.query_params.get('institute', None)
        if institute is not None and self.action == 'list':
            institute = institute.title()
            queryset = queryset.filter(institute_id=institute)
        return queryset

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = SectionSerializer

    def get_queryset(self):
        queryset = Section.objects.all()
        paper = self.request.query_params.get('paper', None)
        if paper is not None and self.action == 'list':
            paper = paper.title()
            queryset = queryset.filter(paper_id=paper)
        return queryset

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]


class ExamViewSet(viewsets.ModelViewSet):
    serializer_class = ExamSerializer

    def get_queryset(self):
        queryset = Exam.objects.all()
        paper = self.request.query_params.get('paper', None)
        if paper is not None and self.action == 'list':
            paper = paper.title()
            queryset = queryset.filter(paper_id=paper)
        return queryset

    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        section = self.request.query_params.get('section', None)
        if section is not None and self.action == 'list':
            section = section.title()
            queryset = queryset.filter(section_id=section)
        return queryset

    permission_classes = [permissions.IsAuthenticated]


class ResultViewSet(viewsets.ModelViewSet):
    serializer_class = ResultSerializer

    def get_queryset(self):
        queryset = Result.objects.all()
        exam = self.request.query_params.get('exam', None)
        student = self.request.query_params.get('student', None)
        if self.action == 'list':
            if exam is not None and student is not None:
                exam = exam.title()
                student = student.title()
                queryset = queryset.filter(exam_id=exam, student_id=student)
            elif exam is not None:
                exam = exam.title()
                queryset = queryset.filter(exam_id=exam)
            elif student is not None:
                student = student.title()
                queryset = queryset.filter(student_id=student)
        return queryset

    permission_classes = [permissions.IsAuthenticated]


class AttemptedQuestionViewSet(viewsets.ModelViewSet):
    serializer_class = AttemptedQuestionSerializer

    def get_queryset(self):
        queryset = AttemptedQuestion.objects.all()
        result = self.request.query_params.get('result', None)
        question = self.request.query_params.get('question', None)
        if self.action == 'list':
            if result is not None and question is not None:
                result = result.title()
                question = question.title()
                queryset = queryset.filter(result_id=result, question_id=question)
            elif result is not None:
                result = result.title()
                queryset = queryset.filter(result_id=result)
            elif question is not None:
                question = question.title()
                queryset = queryset.filter(question_id=question)
        return queryset

    permission_classes = [permissions.IsAuthenticated]


# class StudentList(mixins.CreateModelMixin,
#                     mixins.ListModelMixin,
#                     viewsets.GenericViewSet):
#     serializer_class = StudentSerializer
#
#     def get_queryset(self):
#         return Student.objects.filter(institute_id=self.kwargs['pk'])

