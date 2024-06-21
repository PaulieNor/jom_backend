from rest_framework import serializers
from .models import Job, Category, Company


class JobSerializer(serializers.ModelSerializer):
    company_title = serializers.ReadOnlyField(source='company_id.title')
    img_src = serializers.ReadOnlyField(source='company_id.img_src')

    class Meta:
        model = Job
        fields = (
            'id',
            'title',
            'position_salary',
            'position_location',
            'company_id',
            'company_title',
            'created_at',
            'format_created_at',
            'img_src'
        )

class JobDetailSerializer(serializers.ModelSerializer):
    company_title = serializers.ReadOnlyField(source='company_id.title')
    img_src = serializers.ReadOnlyField(source='company_id.img_src')

    class Meta:
        model = Job
        fields = (
            'id',
            'category',
            'title',
            'description',
            'position_salary',
            'position_location',
            'company_id',
            'company_title',
            'created_at',
            'format_created_at',
            'img_src'
        )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            '__all__'
        )

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'title'
        )