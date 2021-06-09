

def handle_uploaded_file(f):
    with open('run_model/upload_files/upload.dcm', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

        print('upload file saved')


def get_sample_input(f):
    '''
    reference: https://stackoverflow.com/questions/36392510/django-download-a-file
    '''
    import os
    file_path = os.path.join('run_model/SAMPLE_INPUT', '{}.dcm'.format(str(f)))

    return file_path
