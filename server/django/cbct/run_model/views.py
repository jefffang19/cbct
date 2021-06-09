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

        # check if file format is correct
        filename = str(request.FILES['file'])
        print(filename)
        if filename.split('.')[-1] != 'dcm':
            print('Wrong Data format')
            return HttpResponse('Wrong Data format, please upload a .dcm file')

        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('loading')
    else:
        form = UploadFileForm()

    return render(request, 'run_model/upload.html', {'form': form})


def show_result(request):
    return render(request, 'run_model/show_result.html')


def home(request):
    return render(request, 'run_model/index.html')


def loading(request):
    from shutil import copyfile
    import subprocess

    # copy the uploaded dicom file to model input folder
    copyfile('run_model/upload_files/upload.dcm', '../../input/in.dcm')

    # run model
    subprocess.run(['python', '../../inference.py'])

    # copy the result back to server static folder
    copyfile('../../output/ori.jpg', 'run_model/static/run_model/ori.jpg')
    copyfile('../../output/proc.jpg', 'run_model/static/run_model/proc.jpg')

    return render(request, 'run_model/show_result.html')
