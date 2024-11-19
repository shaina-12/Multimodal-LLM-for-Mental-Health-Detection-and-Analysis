import os
os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "3,2,0,1,5,6"
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from datetime import timedelta
from django.utils import timezone
import sys
sys.path.insert(1, '/media/nas_mount/shaina_mehta/baseline/ltu_new/ltu/src/ltu_as')
from ltu_as_inference import get_final_resp
import re

def check_depression_status(response):
    depressed_pattern = r"\b(depressed|feeling\s+down|sad|low)\b"
    not_depressed_pattern = r"\b(not\s+depressed|feeling\s+good|happy|normal)\b"
    
    if re.search(not_depressed_pattern, response, re.IGNORECASE):
        return False
    elif re.search(depressed_pattern, response, re.IGNORECASE):
        return True
    else:
        return None


def index(request):
    return render(request, 'deepltuas/index.html')

@csrf_exempt 
def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        audio_bytes = audio_file.read()
        filename = f"temp_audio_{timezone.now().strftime('%Y%m%d%H%M%S')}.wav"
        file_path = default_storage.save(filename, ContentFile(audio_bytes))
        file_url = default_storage.url(file_path)
        print(file_url)
        response = get_final_resp(file_url)
        #response = "Depressed"
        return JsonResponse({'response': response, 'isDepressed': check_depression_status(response)})
    
    return JsonResponse({'error': 'No audio file uploaded'}, status=400)

