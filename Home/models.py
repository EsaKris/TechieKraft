from django.db import models
from django.core.validators import MinValueValidator
from datetime import date


class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class LGA(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.TextChoices):
    DIRECTOR = 'director', 'School Director'
    PROPRIETOR = 'proprietor', 'Proprietor'
    HEAD_TEACHER = 'head_teacher', 'Head Teacher'


class SchoolType(models.TextChoices):
    PRIMARY = 'primary', 'Primary'
    SECONDARY = 'secondary', 'Secondary'
    PRIMARY_SECONDARY = 'primary_secondary', 'Primary & Secondary'


class YesNoChoice(models.TextChoices):
    YES = 'yes', 'Yes'
    NO = 'no', 'No'


class SchoolRegistration(models.Model):
    first_name = models.CharField(max_length=100, blank=False, verbose_name="First Name")
    last_name = models.CharField(max_length=100, blank=False, verbose_name="Last Name")
    email = models.EmailField(blank=False, unique=True, verbose_name="Email Address")
    phone = models.CharField( max_length=11, blank=False, unique=True, verbose_name="Phone Number")
    school_name = models.CharField(max_length=255, blank=False, verbose_name="School Name")
    position = models.CharField(max_length=50, choices=Position.choices, blank=False)
    school_address = models.CharField(max_length=255, blank=False, verbose_name="School Address")
    state = models.CharField(max_length=100, blank=False, verbose_name="State")
    lga = models.CharField(max_length=100, blank=False, verbose_name="Local Government Area (LGA)")
    landmark = models.CharField(max_length=255, blank=False, verbose_name="Landmark")
    school_type = models.CharField(max_length=50, choices=SchoolType.choices, blank=False)
    laptop = models.CharField(max_length=3, choices=YesNoChoice.choices, blank=False)
    computer_lab = models.CharField(max_length=3, choices=YesNoChoice.choices, blank=False)
    finance_tool = models.CharField(max_length=3, choices=YesNoChoice.choices, blank=False)
    results_tool = models.CharField(max_length=3, choices=YesNoChoice.choices, blank=False)
    cbt_exam = models.CharField(max_length=3, choices=YesNoChoice.choices, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.school_name} ({self.position})"


class Appointment(models.Model):
    school_registration = models.ForeignKey(
        'SchoolRegistration',
        on_delete=models.CASCADE,
        related_name="appointments",  # Optional: for reverse lookup
        null=True,  # Allow nulls temporarily
        blank=True  # Allow blank in forms temporarily
    )
    date = models.DateField(
        validators=[MinValueValidator(limit_value=date.today)]
    )
    time = models.TimeField()

    def __str__(self):
        return f"Appointment for {self.school_registration.first_name} on {self.date} at {self.time}"


