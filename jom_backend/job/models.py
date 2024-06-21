from django.contrib.auth.models import User
from django.db import models
from django.template import defaultfilters

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        ordering = ('title'),


class Company(models.Model):
    title = models.CharField(max_length=255)
    img_src = models.CharField(max_length=255, default = 'https://jomdevassets.s3.eu-west-2.amazonaws.com/OIG+(5).jpg')

    class Meta:
        ordering = ('title'),


class Job(models.Model):
    category = models.ForeignKey(Category, related_name='job', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    position_salary = models.CharField(max_length=255)
    position_location = models.CharField(max_length=255)
    company_id = models.ForeignKey(Company, related_name='job', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    created_by = models.ForeignKey(User, related_name='job', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at', )

    def format_created_at(self):
        return defaultfilters.date(self.created_at, 'd M, Y')