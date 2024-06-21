from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import Job, Category, Company
from .serializer import JobSerializer, JobDetailSerializer, CategorySerializer, CompanySerializer

# Create your views here.


class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)

class BrowseJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()

        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')

        if query:
            jobs = jobs.filter(title__icontains=query)


        if categories:
            jobs = jobs.filter(category_id__in=categories.split(','))

        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)

class CreateJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None)

class JobsDetailView(APIView):
    def get(self, request, pk, format=None):
        job = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(job)

        return Response(serializer.data)

class CompanyView(APIView):
    def get(self, request, pk, format=None):
        company = Company.objects.get(pk=pk)
        serializer = CompanySerializer(company)

        return Response(serializer.data)