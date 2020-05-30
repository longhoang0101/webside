from django import forms
from .models import Contact, CourseReview, BillDetail, Course
from django.contrib.auth.models import User

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["user_id", "contact_name", "contact_mail", "contact_content"]



class ReviewForm(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ["user_id", "course_id", "review_content", "review_star"]

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = BillDetail
        fields = ["user_id", "course_id", "bill_fn", "bill_ln", "bill_mail", "bill_address", "bill_country", "bill_city", "bill_zip"]

class CourseView(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course_id", "course_name", "course_cate_id", "instructor_id", "course_overview", "course_price", "course_image", "course_duration", "course_lecture", "course_quiz", "course_percent_pass", "course_max_retake", "course_long_overview", "course_what_learn"]



