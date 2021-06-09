from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UploadFileForm
from .utils import handle_uploaded_file

# Create your views here.


def run_model(request):
    import subprocess

    # run inference.py
    subprocess.run(['python', '../../inference.py'])

    return HttpResponse('Running Model')


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('interface')
    else:
        form = UploadFileForm()

    return render(request, 'run_model/upload.html', {'form': form})


def interface(request):
    return render(request, 'run_model/interface.html')
