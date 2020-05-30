from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager




class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=127)
    customer_mail = models.CharField(max_length=127)

    def __str__(self):
        return f"{self.customer_id}{self.customer_name}{self.customer_mail}"


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=127)
    contact_mail = models.EmailField()
    contact_content = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contact_id}{self.contact_mail}{self.contact_name}{self.contact_content}"


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=127)

    def __str__(self):
        return self.category_name

class Course_Category(models.Model):
    course_cate_id = models.CharField(max_length=127, primary_key=True)



    course_cate_name = models.CharField(max_length=127)
    course_category_image = models.ImageField(default="NULL")
    course_cate_overview = models.CharField(max_length=127)

    def __str__(self):
        return f"{self.course_cate_id}{self.course_cate_name}{self.course_category_image}{self.course_cate_overview}"


class CourseInstructor(models.Model):
    instructor_id = models.CharField(primary_key=True, max_length=127)
    instructor_name = models.CharField(max_length=127)
    instructor_overview = models.CharField(max_length=500)
    instructor_image = models.ImageField(default="NULL", upload_to='photo/instructor/', blank=True)

    def __str__(self):
        return f"{self.instructor_id}{self.instructor_name}{self.instructor_overview}{self.instructor_image}"


class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=127)
    course_name = models.CharField(max_length=127)
    course_cate_id = models.ForeignKey(Course_Category, on_delete=models.CASCADE, related_name="arrivals")
    instructor_id = models.ForeignKey(CourseInstructor, on_delete=models.CASCADE, related_name="instructor",
                                      default="INS01")
    course_overview = models.CharField(max_length=127)
    course_price = models.IntegerField()
    course_image = models.ImageField(default="NULL", upload_to='photo/', blank=True)
    course_duration = models.CharField(max_length=127, default="NULL")
    course_lecture = models.IntegerField(blank=True, null=True)
    course_quiz = models.IntegerField(blank=True, null=True)
    course_percent_pass = models.IntegerField(blank=True, null=True)
    course_max_retake = models.IntegerField(blank=True, null=True)
    course_long_overview = models.CharField(max_length=2000, default="NULL")
    course_what_learn = models.CharField(max_length=500, default="NULL")

    def __str__(self):
        return f"{self.course_id}{self.course_name}{self.course_cate_id}{self.course_overview}{self.course_price}"


class CourseReview(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    review_star = models.IntegerField()
    review_content = models.CharField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.review_id}{self.user_id}{self.course_id}{self.review_star}{self.review_content}"


class BillDetail(models.Model):
    bill_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    bill_fn = models.CharField(max_length=200)
    bill_ln = models.CharField(max_length=200)
    bill_mail = models.CharField(max_length=200)
    bill_address = models.CharField(max_length=200)
    bill_country = models.CharField(max_length=200)
    bill_city = models.CharField(max_length=200)
    bill_zip = models.CharField(max_length=200)
    bill_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.bill_id}{self.bill_fn}{self.bill_ln}{self.bill_date}"
