from django.urls import path, include
from . import views 

urlpatterns = [
    path('categories', views.CategoriesView.as_view()),
    path('companies/<int:pk>/', views.CompanyView.as_view()),
    path('latest', views.NewestJobsView.as_view()),
    path('all', views.BrowseJobsView.as_view()),
    path('<int:pk>/', views.JobsDetailView.as_view()),
    path('<int:pk>/delete/', views.CreateJobView.as_view()),
    path('<int:pk>/edit/', views.CreateJobView.as_view()),
    ]