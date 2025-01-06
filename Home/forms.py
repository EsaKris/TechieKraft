from django import forms
from .models import SchoolRegistration, Appointment

class SchoolRegistrationForm(forms.ModelForm):
    class Meta:
        model = SchoolRegistration
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'school_name', 'position',
            'school_address', 'state', 'lga', 'landmark', 'school_type',
            'laptop', 'computer_lab', 'finance_tool', 'results_tool', 'cbt_exam'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'last_name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'phone': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'school_name': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'position': forms.Select(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'school_address': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'state': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'lga' : forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'landmark': forms.TextInput(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'school_type': forms.Select(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'laptop': forms.Select(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'computer_lab': forms.Select(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'finance_tool': forms.Select(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'results_tool': forms.Select(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
            'cbt_exam': forms.Select(attrs={'class': 'w-full p-3 border border-gray-700 bg-gray-800 text-gray-200 rounded-md'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)




class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'time']  

    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
