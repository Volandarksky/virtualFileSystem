from django.shortcuts import render
from vfs.models import *

# Create your views here.
def vfs(request):
    # folder = Folder.objects.get()
    return render(request, 'vfs/vfs.html', locals())

def dirs(request):
    folder = Folder.objects.get(path=folder_path)
    return render(request, 'vfs/vfs.html', locals())
