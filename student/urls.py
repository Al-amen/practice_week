from django.urls import path 
from student import views
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
   path("create-student/",views.StudentCreateView.as_view(),name = 'create-student'),
    path("student-details/<int:pk>/",views.StudentDetailsView.as_view(),name = 'student-details'),
    path("student-update/<int:pk>/",views.StudentUpdateView.as_view(),name = 'student-update'),
    path("student-delete/<int:pk>/",views.StudentDeleteView.as_view(),name = 'student-delete'),
    path("search/",views.SearchResultsView.as_view(),name = 'student-search'),
]
