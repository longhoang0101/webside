from django.template.defaulttags import url
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from .login_form import UserLoginForm
from .views import delete_view, update_view
from . import views


urlpatterns = [
    path("",views.index, name="base"),
    #path('/signup', views.registerView, name="register_url"),
    path("danhsachkhoahoc", views.khoahoc, name="DanhSach"),
    path("tintuc", views.tintuc, name="Tintuc"),
    path(
        'ins_login/', views.InstructorLoginView, name="ins_login"
    ),

    path('change-password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html')),
    path('registration/register', views.UserRegister, name='register'),
    path("course_overview/<str:course_id>", views.course_overview, name="course_ovv"),
    path("test", views.test, name="test"),
    path("contact", views.ContactView, name="contact"),
    path("checkout/<str:course_id>", views.checkout, name="checkout"),
    path("nganhhoc/<str:course_cate_id>", views.nganh_hoc, name="nganhhoc"),
    path("instructor", views.instructor, name="instructor"),
    path("payment_succesful", views.payment_successful, name="payment_successful"),

    path("ins_index", views.ins_index, name="ins_index"),
    path("add_course", views.add_new_course, name="add_course"),
    path("ins_register", views.InstructorRegister, name="ins_register"),
    path('<course_id>/delete', delete_view),
    path('<course_id>/update', update_view),

]
