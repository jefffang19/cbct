

def handle_uploaded_file(f):
    with open('run_model/upload_files/upload.dcm', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

        print('upload file saved')
