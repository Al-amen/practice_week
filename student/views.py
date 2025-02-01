from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
    
)
from student.models import Student
from django.contrib import messages
from student.forms import StudentForm
from django.db.models import Q


class HomeView(ListView):
    template_name = 'student/home.html'
    model = Student
    context_object_name = 'students'

class StudentCreateView(CreateView):
    template_name = 'student/student_form.html'
    model = Student
    form_class = StudentForm
    #fields = ['name','email','phone_number','course']
    success_url = '/'
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student created successfully')
        return response


class StudentDetailsView(DetailView):
    template_name = 'student/student_details.html'
    model = Student
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    template_name = 'student/student_form.html'
    model = Student
    form_class = StudentForm
    success_url = '/'
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Student updated successfully')
        return response 

class StudentDeleteView(DeleteView):
    template_name = 'student/student_details.html'
    model = Student
    success_url = '/'
    def get(self, request, *args, **kwargs):
        student = self.get_object()
        student.delete()
        messages.success(request, "Student has been deleted successfully!")
        return HttpResponseRedirect(self.success_url)

class SearchResultsView(ListView):
    model = Student
    template_name = 'student/student_search.html'
    context_object_name = 'students'
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:

            return Student.objects.filter(
                Q(name__icontains=query) | 
                Q(course__icontains=query)|
                Q(email__icontains=query)|
                Q(phone_number__icontains=query)|
                Q(student_Id__icontains=query)

            )
        return Student.objects.none()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context
   