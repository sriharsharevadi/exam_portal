from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.auth.models import User


class BaseUser(AbstractUser):
    is_institute = models.BooleanField(default=False)


class Institute(models.Model):
    SUBSCRIPTION_CHOICES = [
        ('d', 'Default')
    ]
    user_id = models.ForeignKey(BaseUser, related_name='institute_user', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True)
    is_verified = models.BooleanField(default=False)
    subscription = models.CharField(max_length=2, choices=SUBSCRIPTION_CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    state= models.CharField(max_length=255, blank=True)
    mobile = PhoneNumberField(blank=True, max_length = 15)
    alternate_mobile = PhoneNumberField(blank=True, max_length = 15)
    student_cap = models.IntegerField(blank=True)
    expiry_date = models.DateField(blank=True)

    def __str__(self):
        return self.name


class Batch(models.Model):
    name = models.CharField(max_length=255, blank=True)
    institute_id = models.ForeignKey(Institute, related_name='batch_institute', on_delete=models.CASCADE)
    start_time = models.DateField(blank=True)
    end_time = models.DateField(blank=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    user_id = models.ForeignKey(BaseUser, related_name='student_user', on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=30, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    institute_id = models.ForeignKey(Institute, related_name='student_institute', on_delete=models.CASCADE)
    batch_id = models.ForeignKey(Batch, on_delete=models.CASCADE)
    city = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)
    mobile = PhoneNumberField(blank=True, max_length=15)
    expiry_date = models.DateField(blank=True)

    def __str__(self):
        return self.first_name


class Paper(models.Model):
    EXAM_CHOICES = [
        ('m', 'JEE MAINS'),
        ('a', 'JEE ADVANCED'),
        ('o', 'OTHERS')
    ]
    institute_id = models.ForeignKey(Institute, related_name='paper_institute', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    exam_type = models.CharField(max_length=1, choices=EXAM_CHOICES, blank=True)

    def __str__(self):
        return self.name


class Section(models.Model):
    SECTION_CHOICES =[
        ('m', 'MATHS'),
        ('p', 'PHYSICS'),
        ('c', 'CHEMISTRY')
    ]
    paper_id = models.ForeignKey(Paper, related_name='section_paper', on_delete=models.CASCADE)
    name = models.CharField(max_length=1, choices=SECTION_CHOICES, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    QUESTION_CHOICES = [
        ('s', 'SINGLE CORRECT ANSWER'),
        ('p', 'INTEGER TYPE'),
        ('c', 'MULTIPLE CORRECT ANSWER')
    ]
    section_id = models.ForeignKey(Section, related_name='question_section', on_delete=models.CASCADE)
    question_type = models.CharField(max_length=1, choices=QUESTION_CHOICES, blank=True)
    max_marks = models.IntegerField(blank=True)
    max_marks = models.IntegerField(blank=True)
    question = models.CharField(max_length=255, blank=True)
    option_1 = models.CharField(max_length=255, blank=True)
    option_2 = models.CharField(max_length=255, blank=True)
    option_3 = models.CharField(max_length=255, blank=True)
    option_4 = models.CharField(max_length=255, blank=True)
    image_url= models.CharField(max_length=255, blank=True)
    correct_answer = models.IntegerField(blank=True)

    def __str__(self):
        return self.id


class Exam(models.Model):
    paper_id = models.ForeignKey(Paper, related_name='exam_paper', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    live_from = models.DateField(blank=True)
    live_to = models.DateField(blank=True)
    batches = models.ManyToManyField(Batch)
    duration = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Result(models.Model):
    exam_id = models.ForeignKey(Exam, related_name='result_exam', on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, related_name='result_student', on_delete=models.CASCADE)
    started = models.DateField(blank=True)
    ended = models.DateField(blank=True)
    marks_secured = models.IntegerField(blank=True)

    def __str__(self):
        return self.id


class AttemptedQuestion(models.Model):
    result_id = models.ForeignKey(Result, related_name='attempted_question_result', on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, related_name='attempted_question_question', on_delete=models.CASCADE)
    answer_given = models.IntegerField(blank=True)
    marks_secured = models.IntegerField(blank=True)
    time_taken = models.IntegerField(blank=True)

    def __str__(self):
        return self.id









