from rest_framework import serializers
from .models import Institute, Student, Batch, Paper,  Section, Question, Exam, Result, AttemptedQuestion, BaseUser
from django.contrib.auth.models import Group


class BaseUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseUser
        fields = ['url', 'username', 'email', 'groups', 'is_institute']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'


class BatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Batch
        fields = '__all__'


class PaperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Paper
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class AttemptedQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttemptedQuestion
        fields = '__all__'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class InstituteSerializer(serializers.ModelSerializer):
    # student_institute = StudentSerializer(many=True, read_only=True)
    # batch_institute = BatchSerializer(many=True, read_only=True)

    class Meta:
        model = Institute
        fields = '__all__'


