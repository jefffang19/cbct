from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def run_model(request):
    import subprocess

    # run inference.py
    subprocess.run(['python', '../../inference.py'])

    return HttpResponse('Running Model')


def interface(request):
    return render(request, 'run_model/interface.html')
