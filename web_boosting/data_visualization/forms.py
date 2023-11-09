from django.forms import ModelForm
from .models import DiabetesFromCsv

class DiabetesImportForm(ModelForm):
    class Meta:
        model = DiabetesFromCsv
        fields = ('csv_file',)