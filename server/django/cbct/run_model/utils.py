def handle_uploaded_file(f):
    with open('run_model/upload_files/upload.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

        print('upload file saved')
