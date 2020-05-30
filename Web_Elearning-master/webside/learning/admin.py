from django.contrib import admin

from .models import Customer
from .models import Course
from .models import Course_Category, Contact, CourseInstructor,CourseReview, BillDetail

# Register your models here.



admin.site.register(Course)
admin.site.register(Course_Category)
admin.site.register(Contact)
admin.site.register(CourseInstructor)
admin.site.register(CourseReview)
admin.site.register(BillDetail)
