from django.contrib import admin
from .models import BaseUser, Institute, Student, Batch, Paper, Section, Question, Exam, Result, AttemptedQuestion
admin.site.register(BaseUser)
admin.site.register(Institute)
admin.site.register(Student)
admin.site.register(Batch)
admin.site.register(Paper)
admin.site.register(Section)
admin.site.register(Question)
admin.site.register(Exam)
admin.site.register(Result)
admin.site.register(AttemptedQuestion)

