import io
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Activity
from googleapiclient.discovery import build
from google.oauth2 import service_account
from .forms import ActivityForm
from django.core.files.uploadedfile import SimpleUploadedFile
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseUpload


def index(request):
    return render(request, "base/index.html")

def success(request):
     return render(request,"base/sucess.html")


def get_name(request):
    if request.method == "POST":
        form = ActivityForm(request.POST,request.FILES)
        if form.is_valid():
            id =upload(form.cleaned_data['file'].read(),request.user.admission_number)
            print("https://drive.google.com/file/d/{id}/preview".format(id=id))
            return HttpResponseRedirect("/sucess")

    else:
        form = ActivityForm()

    return render(request, "base/homepage.html", {"form": form})


def upload(files,name):


    SCOPES = ['https://www.googleapis.com/auth/drive']
    SERVICE_ACCOUNT_FILE = 'base/credentials.json'

    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    file_metadata = {'name': '{name}.jpg'.format(name=name),'parents':['1uyA4MF7mJMUplqzpnsTh5C3OAPM5qnTv'],}
    media = MediaIoBaseUpload(io.BytesIO(files),mimetype='image/jpeg')

    file = service.files().create(body=file_metadata, media_body=media,fields='id').execute()
    return file.get("id")
    