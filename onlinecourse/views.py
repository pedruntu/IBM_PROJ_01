from django.shortcuts import render
from django.http import HttpResponseRedirect
# <HINT> Import any new Models here
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, logout, authenticate
import logging
from .models import Course, Enrollment, Question, Choice, Submission, Answer
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'onlinecourse/user_registration_bootstrap.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("onlinecourse:index")
        else:
            context['message'] = "User already exists."
            return render(request, 'onlinecourse/user_registration_bootstrap.html', context)


def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('onlinecourse:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'onlinecourse/user_login_bootstrap.html', context)
    else:
        return render(request, 'onlinecourse/user_login_bootstrap.html', context)


def logout_request(request):
    logout(request)
    return redirect('onlinecourse:index')


def check_if_enrolled(user, course):
    is_enrolled = False
    if user.id is not None:
        # Check if user enrolled
        num_results = Enrollment.objects.filter(user=user, course=course).count()
        if num_results > 0:
            is_enrolled = True
    return is_enrolled


# CourseListView
class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list_bootstrap.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        user = self.request.user
        courses = Course.objects.order_by('-total_enrollment')[:10]
        for course in courses:
            if user.is_authenticated:
                course.is_enrolled = check_if_enrolled(user, course)
        return courses

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_detail_bootstrap.html'

def enroll(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    is_enrolled = check_if_enrolled(user, course)
    if not is_enrolled and user.is_authenticated:
        # Create an enrollment
        Enrollment.objects.create(user=user, course=course, mode='honor')
        course.total_enrollment += 1
        course.save()

    return HttpResponseRedirect(reverse(viewname='onlinecourse:course_details', args=(course.id,)))

# Submit view, exam submission
def submit(request, course_id):
    #context = {}
    user = request.user
    course = get_object_or_404(Course, pk=course_id)    
    print('When click on submit button')
    print('Course N°:', course_id, 'Name:',course.name)
    print('User N°:', user.id, user.username,user.first_name, user.last_name)
    enrollment=Enrollment.objects.get(course=course_id, user=user.id)
    print('Enrollment ID:',enrollment.id, 'User:', enrollment.user_id, 'mode:',enrollment.mode)
    
    #Create Submission object
    submission= Submission.objects.create(enrollment_id= enrollment.id)
    print('Submission ID:', submission.id)
    # Now collect selected choices and create Answer objects
    print('Answers form form:')
    selected_choices=extract_answers(request)
    for selected_choice in selected_choices:   
        choice = Choice.objects.get(pk=selected_choice)                         
        answer= Answer.objects.create(submission= submission, choice= choice ) #it must be an instance         
        print('Created Answer ID:', answer.id, 'Choice:', answer.choice_id)             
    return redirect('onlinecourse:show_exam_result',course_id, submission.id)

    
# A example method to collect the selected choices from the exam form from the request object
def extract_answers(request):
    submitted_anwsers = []
    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST[key]
            choice_id = int(value)
            submitted_anwsers.append(choice_id)
    return submitted_anwsers


# <HINT> Create an exam result view to check if learner passed exam and show their question results and result for each question,
# you may implement it based on the following logic:
        # Get course and submission based on their ids
        # Get the selected choice ids from the submission record
        # For each selected choice, check if it is a correct answer or not
        # Calculate the total score
def show_exam_result(request, course_id, submission_id):
    print('Arrived to show exam view')
    context={}
    course = get_object_or_404(Course, pk=course_id)
    questions= Question.objects.filter(course_id=course_id)    
    submission = get_object_or_404(Submission, pk=submission_id)    
    answs_subm=Answer.objects.filter(submission=submission_id)    
    print('Course:',course.id,' Questions:',questions.count(),' Submission:',submission.id,' Answers:',answs_subm.count()) 
    
    # Process submitted answers
    total_score=0 ; base_score=0; sel_choi={}; q_corr={}

    for question in questions:
        for an_q in Choice.objects.filter(question=question.id):
            sel_choi[an_q.id]= False   
        ans4check=[]
        for answ_subm in answs_subm:            
            #print('Answer ID:',answ_subm.id,' Choice ID:', answ_subm.choice_id)             
            choi= Choice.objects.get(id=answ_subm.choice_id)                             
            print(' SelectedChoice ID:', answ_subm.choice_id,'From question:',choi.question_id)
            if choi.question_id==question.id:
                ans4check.append(answ_subm.choice_id)
                sel_choi[answ_subm.choice_id]=True              

        is_corr= Question.is_get_score( question,ans4check)
        print('Question:',question.id, 'Answers',ans4check,' Is correct?',is_corr)
        base_score=base_score+question.grade
        if is_corr: 
            total_score=total_score+question.grade
            q_corr[question.id]=True
        else:
            q_corr[question.id]=False

        
        
    #print('Exam Total Score:', total_score,' Base Score:',base_score) 
    #print(sel_choi[1],sel_choi[2],sel_choi[4])
    #print('Correct Questions:',q_corr)
    #print('Choices',sel_choi)

    context={'course': course,  'grade': total_score,'base':base_score, 'q_corr':q_corr,'sel_choi':sel_choi}
 
    

    
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html',context)
    
    #return render(request, "onlinecourse/Hello.html")




