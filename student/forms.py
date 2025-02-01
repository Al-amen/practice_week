from student.models import Student

from django import forms

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_Id','name','email','phone_number','course']

        labels = {
            'student_Id': 'Student ID',
            'name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'course': 'Course',
              # Unique ID for each student
        }
    
        widgets = {
            'student_Id': forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your student id'}),
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your full name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your email address'}),
            'phone_number': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your phone number'}),
            'course': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your course'}),
            
        }
