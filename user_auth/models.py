# from django.db import models
# from django.contrib.auth.models import AbstractUser

# class Student(AbstractUser):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     student_no = models.PositiveIntegerField(unique=True)
#     # username = None
    

#     USERNAME_FIELD = 'student_no'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return f' email: {self.email}'

