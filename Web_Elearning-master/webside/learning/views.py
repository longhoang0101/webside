from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .forms import ContactForm, ReviewForm, CheckOutForm, CourseView
from django.contrib.auth.models import Group
from .login_form import LoginForm, UserLoginForm
from .models import Course, CourseReview, Course_Category, CourseInstructor
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect
from django.conf import settings

# Create your views here.


def index(request):
    return render(request, "learning/index.html")


def khoahoc(request):
    return render(request, "learning/khoahoc.html")


def payment_successful(request):
    return render(request, "learning/payment_succesful.html")




def tintuc(request):
    return render(request, "learning/tintuc.html")


def test(request):
    return render(request, "learning/test.html")



def UserRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='NormalCustomer')
            user.groups.add(group)
            messages.success(request, 'Tạo tài khoản thành công')
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def InstructorLoginView(request):
    error = ''
    form = UserLoginForm(request.POST)
    if request.method == 'POST':

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponseRedirect("/contact",
                                                settings.LOGIN_REDIRECT_URL)
            else:
                error = 'Tài khoản hoặc mật khẩu sai!'
                form = UserLoginForm()
    return render(request, "learning/instructor_login.html", {"form" : form, "error" : error})


'''
def flight(request, flight_id):
    try:
        flight = Course_Category.objects.get(pk=flight_id)
    except Course_Category.DoesNotExist:
        raise Http404("Flight does not exit.")
    context = {
        "flight": flight,
        "passengers": flight.passengers.all(),

    }
    return render(request, "/learning", context)
'''
'''

'''


def khoahoc(request):
    course = Course.objects.all()
    return render(request, "learning/khoahoc.html", {"course": course})



def index(request):
    context = {
        "courses": Course.objects.all(),
     }
    return render(request, "learning/index.html", context)


def course_overview(request, course_id):
    comment = CourseReview.objects.filter(course_id=course_id).order_by('-date_created')
    form = ReviewForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Gửi thành công !!!')

    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Khóa học không tồn tại.")
    context = {
        "course": course,
        "form": form,
        "comment": comment,

    }
    return render(request, "learning/course_overview.html", context)


def checkout(request, course_id):
    form = CheckOutForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Lưu hóa đơn thành công !!!')
        return redirect('/payment_succesful')
    try:
        course = Course.objects.get(pk=course_id)
    except Course.DoesNotExist:
        raise Http404("Khóa học không tồn tại.")
    context = {
        "course": course,
        "form" : form
    }
    return render(request, "learning/checkout.html", context)



def ContactView(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Gửi thành công !!!')
    else:
        error = 'Thông tin nhập không hợp lệ!'
        form = ContactForm()
    context = {'form': form}

    return render(request, 'learning/contact.html', context)


def nganh_hoc(request, course_cate_id):
    courses = Course.objects.filter(course_cate_id=course_cate_id)
    temp = Course_Category.objects.get(course_cate_id = course_cate_id)
    return render(request, "learning/nganh_hoc.html", {"courses": courses, "nganhhoc" : temp})

def instructor(request):
    ins = CourseInstructor.objects.all()
    context = {
        "ins" : ins
    }
    return render(request, "learning/instructor.html", context)


def add_new_course(request):
    message = ''
    form = CourseView(request.POST)
    if form.is_valid():
        form.save()
        message = 'Lưu khóa học thành công !!!'
        return redirect('/ins_index')
    course = Course.objects.all()
    context = {
        "course": course,
        "form" : form,
        "message" :message
    }
    return render(request, "learning/ins_add_course.html", context)


def ins_index(request):

    course = Course.objects.all()
    #usr = User.objects.filter(username=username).filter(groups__name='Instructor')
    #if usr.exists():
        #mess = True
    #else:
        #mess = False
    context = {
        "course" : course
    }
    return render(request, "learning/instructor_index.html", context)


def delete_view(request, course_id):
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Course, course_id=course_id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/ins_index")

    return render(request, "learning/delete_view.html", context)


def update_view(request, course_id):

    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Course, course_id = course_id)

    # pass the object as instance in form
    form = CourseView(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/ins_index")

    context["form"] = form

    return render(request, "learning/update_view.html", context)

def InstructorRegister(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Instructor')
            user.groups.add(group)
            messages.success(request, 'Tạo tài khoản giảng viên thành công')
            return redirect('/accounts/login')
    else:
        form = UserCreationForm()
    return render(request, 'learning/instructor_register.html', {'form': form})

