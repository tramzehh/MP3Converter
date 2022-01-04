from django.shortcuts import render
import os
from moviepy.editor import *
from django.views import View
from django.http import JsonResponse, HttpResponse
from convert.forms import LinkForm
from django.template.loader import render_to_string
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
class ConverterPage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'convert/home.html')
    
def convert_video_to_mp3(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        filename = os.path.basename(url).split('.')[0]
        clip = VideoFileClip(url)
        audio = clip.audio
        media_dir = os.path.join(settings.MEDIA_ROOT, f'{filename}.mp3')
        print(media_dir)
        audio.write_audiofile(media_dir)
        clip.close()
        audio.close()
        return render(request, 'convert/home.html')

