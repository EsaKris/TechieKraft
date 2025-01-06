import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import SchoolRegistration, Appointment


def download_registered_people(modeladmin, request, queryset):
    # Create a response with CSV file content type
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="registered_people.csv"'

    # Write the CSV headers
    writer = csv.writer(response)
    writer.writerow([
        'First Name', 'Last Name', 'Email', 'Phone', 'School Name', 'Position', 
        'School Address', 'State', 'LGA', 'Landmark', 'School Type', 'Laptop', 
        'Computer Lab', 'Finance Tool', 'Results Tool', 'CBT Exam'
    ])

    # Write data for each selected record
    for registration in queryset:
        writer.writerow([
            registration.first_name, registration.last_name, registration.email, 
            registration.phone, registration.school_name, registration.position,
            registration.school_address, registration.state, registration.lga, 
            registration.landmark, registration.school_type, registration.laptop,
            registration.computer_lab, registration.finance_tool, registration.results_tool,
            registration.cbt_exam
        ])

    return response


# SchoolRegistrationAdmin class with the custom action
class SchoolRegistrationAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "school_name")
    actions = [download_registered_people]  # Add the custom action to the list of actions

# AppointmentAdmin class with custom methods for displaying name and position
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("get_name", "get_position", "date", "time")

    @admin.display(ordering="school_registration__first_name", description="Name")
    def get_name(self, obj):
        return f"{obj.school_registration.first_name} {obj.school_registration.last_name}"

    @admin.display(ordering="school_registration__position", description="Position")
    def get_position(self, obj):
        return obj.school_registration.position


# Register the models with their corresponding admin classes
admin.site.register(SchoolRegistration, SchoolRegistrationAdmin)
admin.site.register(Appointment, AppointmentAdmin)
