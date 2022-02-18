from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Enrollment, Lesson, Instructor, Learner
from .models import Question, Choice,Submission, Answer
# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 5


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 3

class EnrollmentInline(admin.StackedInline):
    model = Enrollment
    extra = 4

class SubmissionInline(admin.StackedInline):
    model = Submission
    extra = 5

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 4

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [EnrollmentInline, LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class EnrollmentAdmin(admin.ModelAdmin):
    inlines = [SubmissionInline]
    list_display = ('course_id','user_id')


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# <HINT> Register Question and Choice models here
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade')
    #list_filter = ['pub_date']
    #search_fields = ['name', 'description']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'is_correct')

class SubmissionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    #list_display = ('course.name', 'user.username')
    list_display = ('id', 'enrollment_id')
    #list_filter = ['pub_date']
    #search_fields = ['name', 'description']

"""
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('submission_id', 'choice_id')
"""

"""
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user')
"""





admin.site.register(Course, CourseAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(Submission, SubmissionAdmin)
#admin.site.register(Answer, AnswerAdmin)