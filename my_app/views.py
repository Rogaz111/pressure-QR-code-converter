import csv
import json
import os
import openpyxl
import qrcode
from django.conf import settings
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
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
    print(pressure_reading.values())
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

    return render(request, "my_app/capture_pressure.html")


# Data Import Route
def import_view(request):
    if request.method == "POST":

        # GET Uploaded File Type
        input_type = request.POST.get('inputType')

        # GET media content
        uploaded_file = request.FILES.get('import_file')

        # If no File Upload or Type Specified return Flash Message to user
        if not uploaded_file or not input_type:
            messages.error(request, "No file selected. Please select a file to upload.")
            return render(request, "my_app/imports.html")

        # Save the uploaded file temporarily
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_path = fs.path(filename)

        # Process Imported Data CSV and XLSX
        if input_type == "csv":
            try:
                with open(file_path, mode='r') as file:
                    csv_file = csv.reader(file)
                    next(csv_file)  # Skip the header
                    for line in csv_file:
                        #CSV is expected as data/pressure_data.csv
                        form_data = {
                            'sample_number': line[0],
                            'fruit_type': line[1],
                            'reading_1': line[2],
                            'reading_2': line[3],
                            'capture_date': line[4],
                            'sample_status': line[5],
                            'capture_station': line[6],
                        }
                        form = PressureReadingForm(form_data)
                        if form.is_valid():
                            form.save()
                        else:
                            messages.warning(request, f"Invalid data in row: {line}")
                messages.success(request, "CSV file imported successfully!")
            except Exception as e:
                messages.error(request, f"An error occurred while processing the CSV file: {str(e)}")

        else:
            if input_type == "xlsx":
                try:
                    wb = openpyxl.load_workbook(file_path)
                    sheet = wb.active
                    for row in sheet.iter_rows(min_row=2, values_only=True):
                        # Assuming the XLSX is formatted according to data/pressure_data.xlsx
                        form_data = {
                            'sample_number': row[0],
                            'fruit_type': row[1],
                            'reading_1': row[2],
                            'reading_2': row[3],
                            'capture_date': row[4],
                            'sample_status': row[5],
                            'capture_station': row[6],
                        }
                        form = PressureReadingForm(form_data)
                        if form.is_valid():
                            form.save()
                        else:
                            messages.warning(request, f"Invalid data in row: {row}")
                    messages.success(request, "XLSX file imported successfully!")
                except Exception as e:
                    messages.error(request, f"An error occurred while processing the XLSX file: {str(e)}")

        return render(request, "my_app/imports.html")
    else:
        return render(request, "my_app/imports.html")


# QR Generation Route
@csrf_exempt
def generate_qr_code(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            body = json.loads(request.body)

            # Extract fields from the JSON object
            qr_data = (
                f"ID: {body.get('ID')}, "
                f"Sample Number: {body.get('Sample Number')}, "
                f"Fruit Type: {body.get('Fruit Type')}, "
                f"Reading 1: {body.get('Reading 1')}, "
                f"Reading 2: {body.get('Reading 2')}, "
                f"Capture Date: {body.get('Capture Date')}, "
                f"Sample Status: {body.get('Sample Status')}, "
                f"Capture Station: {body.get('Capture Station')}"
            )

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)

            # Save QR code image
            img = qr.make_image(fill_color="black", back_color="white")
            filename = f"qr_code_{body.get('Sample Number')}.png"
            qr_code_path = os.path.join(settings.MEDIA_ROOT, "qr_codes", filename)

            os.makedirs(os.path.dirname(qr_code_path), exist_ok=True)  # Ensure directory exists
            img.save(qr_code_path)

            # Return the QR code URL
            qr_code_url = f"{settings.MEDIA_URL}qr_codes/{filename}"

            #Query passed ID to update record with the QR code URL
            if qr_data:
                sample_ = PressureReading.objects.get(id=body.get('ID'))
                if sample_:
                    sample_.qr_code_data = qr_code_url
                    sample_.save()

            return JsonResponse({'message': 'QR Code generated successfully', 'qr_code_url': qr_code_url})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)