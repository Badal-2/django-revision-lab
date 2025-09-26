from django.shortcuts import render,redirect
from .models import *
from .forms import *

from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse, Http404
import os, mimetypes
from django.conf import settings


def list(request):
    em=Employee.objects.all()                    # Data Fetching From Model
    return render(request,"list.html",{"em":em})




def add_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    else:
        form = EmployeeForm()
    return render(request, "employee.html", {"form": form})







# Upload Images and Download Images.


def upload_image(request):
    if request.method == "POST":
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')   # redirect to list after upload
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

def gallery(request):
    photos = Photo.objects.all().order_by('-uploaded_at')
    return render(request, 'gallery.html', {'photos': photos})

def download_image(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    file_path = photo.image.path  # safe: ImageField provides .path in local storage
    if not os.path.exists(file_path):
        raise Http404("File not found")

    mime_type, _ = mimetypes.guess_type(file_path)
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Type'] = mime_type or 'application/octet-stream'
    response['Content-Length'] = os.path.getsize(file_path)
    response['Content-Disposition'] = f'attachment; filename="{os.path.basename(file_path)}"'
    return response
















