from django import forms
from .models import PressureReading


#Form for capturing pressure data
class PressureReadingForm(forms.ModelForm):
    class Meta:
        model = PressureReading
        fields = [
            'sample_number',
            'fruit_type',
            'reading_1',
            'reading_2',
            'capture_date',
            'sample_status',
            'capture_station',
        ]
        widgets = {
            'capture_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }