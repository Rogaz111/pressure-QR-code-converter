from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from my_app.forms import PressureReadingForm
from my_app.models import PressureReading


# Home Page Route
def home(request):
    #Query Data on load
    pressure_reading = PressureReading.objects.all()

    # Pass the data to the template using context
    context_data = {
        'pressure_readings': pressure_reading,
    }
    return render(request, "my_app/home.html", context=context_data)


# Capture Pressures Route
def capture_pressure(request):
    if request.method == 'POST':
        form = PressureReadingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form submitted successfully")
        else:
            messages.warning(request, "Form Validation Failed. Please fill in all required fields")
    else:
        form = PressureReadingForm()
    return render(request, "my_app/capture_pressure.html")


# CSV Import Route
def import_view(request):
    return render(request, "my_app/imports.html")