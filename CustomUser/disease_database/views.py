import json

from django.shortcuts import render
from django.contrib import messages
from django.template.context_processors import csrf

from .forms import DiseaseSearchForm
from .models import Symptom
from .prediction import GenerateMLModel


def SearchView(request):
    # symptom list for symptom options for patient
    symptom_objects = Symptom.objects.all()
    symptom_list = []
    for i in symptom_objects:
        symptom_list.append(i.symptom)
    upload_form = DiseaseSearchForm()

    upload_template = 'search_disease.html'
    return render(request, upload_template, {'upload_form': upload_form, 'symptom_list': symptom_list})


def disease_list_view(request):
    predictions = {}
    if request.is_ajax() and request.method == 'POST':
        symptom_list = json.loads(request.POST.get('symptom_list'))
        predictions = GenerateMLModel(symptom_list)  # supply user symptoms as parameters
        if not predictions:
            # if dictionary is empty means one of the file is missing
            messages.error(request, 'Missing Files in DB')
        else:
            # predicted dictionary is here
            messages.success(request, 'Successfully predicted')
    else:
        messages.success(request, 'This is not ajax request')
    return render(request, 'ajax_prediction_result.html', {'predictions': predictions})

'''
def FileUpload(request):
    if request.method == 'POST' and 'fileUpload_button' in request.POST:
        upload_form = DiseaseSearchForm(request.POST, request.FILES)
        if upload_form.is_valid():
            fileType = request.POST.get('File_Type')
            filePath = request.FILES['File_Path']

            if filePath.name.endswith('.csv'):
                upload_form.save()
                messages.success(request, 'Successfully added to database')
            else:
                messages.error(request, 'These are not CSV file')
        else:
            messages.error(request, 'Invalid form')
'''


