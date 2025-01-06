from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SchoolRegistrationForm, AppointmentForm
from .models import SchoolRegistration, Appointment
from datetime import date
from django.views.decorators.csrf import csrf_protect


def home(request):
    return render(request, 'home/home.html')


@csrf_protect
def register(request):
    if request.method == "POST":
        form = SchoolRegistrationForm(request.POST)
        if form.is_valid():
            
            registration = form.save()  
           
            return redirect("book_appointment", school_registration_id=registration.id)
        else:
            return render(request, "home/register.html", {"form": form})
    else:
        form = SchoolRegistrationForm()

        
    return render(request, "home/register.html", {"form": form})


def book_appointment(request, school_registration_id):
    try:
        school_registration = SchoolRegistration.objects.get(id=school_registration_id)
    except SchoolRegistration.DoesNotExist:
        return render(request, "error.html", {"message": "Registration not found."})

    if request.method == "POST":
        date = request.POST.get("date")
        time = request.POST.get("time")

        Appointment.objects.create(
            school_registration=school_registration,
            date=date,
            time=time
        )
        return redirect("success")

    return render(request, "home/book_appointment.html", {'school_registration_id': school_registration_id})



def success_view(request):
    return render(request, 'home/success.html')
