import os

from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from pyfcm import FCMNotification
from . import models

# Create your views here.
#파이어베이스 키 설정
#APIKEY = "Server Key"
#TOKEN = "Token"

#push_service = FCMNotification(APIKEY)

@csrf_exempt
def getloc(request):
    #global lat
    #global long
    if request.method == 'POST':
        userId = request.POST.get('idStr')
        lat = request.POST.get('lat')
        long = request.POST.get('long')
        try:
            _id = models.Location.objects.get(userId=userId)
        except:
            _id = None
        if _id is None:
            location = models.Location(
                userId=userId,
                lat=lat,
                long=long
            )
            location.save()
        else:
            location = models.Location.objects.get(userId=userId)
            location.lat = lat
            location.long = long
            location.save()
        print(str(lat))
        print(str(long))
    return JsonResponse({'msg': 1}, status=200)
    #return redirect('petsitter:send')

def send(request):
    #파이어베이스로 알림 호출
    #data_message = {
    #    "body": "위치 요청",
    #    "title": "고객님으로부터 위치 정보 요청이 있습니다"
    #}

    #result = push_service.single_device_data_message(registration_id=TOKEN, data_message=data_message)
    if request.method == 'POST':
        otherId = request.POST.get('idStr')
    location = models.Location.objects.get(userId=otherId)
    return JsonResponse({'lat': location.lat, 'long': location.long}, status=200)

@csrf_exempt
def uploadFile(request):
    fileTitle = request.POST["fileTitle"]
    uploadedFile = request.FILES["uploadedFile"]

    #DB에 파일의 정보를 저장
    document = models.Document(
        title=fileTitle,
        uploadedFile=uploadedFile
    )
    document.save()
    #documents = models.Document.objects.all()
    return JsonResponse({'id': document.id, 'title': document.title, 'date': document.dateTimeOfUpload.strftime('%m-%d %H:%M')}, status=200)

def downloadFile(request):
    #파일 다운로드 기능 구현
    file_path = os.path.abspath("media/Uploaded Files/")
    file_name = os.listdir("media/Uploaded Files/")
    fs = FileSystemStorage(file_path)
    response = FileResponse(fs.open(file_name[0], 'rb'), content_type='video/*')
    response['Content-Disposition'] = 'attachment; filename="downloaded.mp4"'
    return response

'''
def practice(request):
    return render(request, 'test/download.html')
'''

