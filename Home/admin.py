from django.contrib import admin
from .models import SchoolRegistration, Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("get_name", "get_position", "date", "time")

    @admin.display(ordering="school_registration__first_name", description="Name")
    def get_name(self, obj):
        return f"{obj.school_registration.first_name} {obj.school_registration.last_name}"

    @admin.display(ordering="school_registration__position", description="Position")
    def get_position(self, obj):
        return obj.school_registration.position


admin.site.register(SchoolRegistration)
admin.site.register(Appointment, AppointmentAdmin)
