# from django.db import models
# from django.db import models
# from django.conf import settings
# from django.dispatch import receiver
# from django.db.models.signals import pre_save, post_save


# # Create your models here.
# class Registration(models.Model):
#     full_name = models.CharField(max_length=200)
#     mobile_number = models.IntegerField()
#     email_address = models.EmailField(max_length=100, null=True, blank=True)
#     password = models.CharField(max_length=100, null=True, blank=True)
#     confirm_password = models.CharField(max_length=100, null=True, blank=True)
#     user_gender = models.CharField(max_length=100, null=True, blank=True)
#     # registered_date = models.DateTimeField()
    
#     def __str__(self):
#         return self.full_name