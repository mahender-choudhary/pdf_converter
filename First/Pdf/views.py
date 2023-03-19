from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def merge(request):
    # print(request.POST['myfile'])
    return render(request, 'merge.html')

def split(request):
    return render(request, 'split.html')

def splitFile(request):
    return render(request, 'split.html')