import os.path

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from PyPDF2 import PdfReader, PdfWriter
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def merge(request):
    # print(request.POST['myfile'])
    return render(request, 'merge.html')

def split(request):
    return render(request, 'split.html')

def compress(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        filePath = fs.url(filename)
        filePath = filePath[1:]
        reader = PdfReader(filePath)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.add_metadata(reader.metadata)
        str = filePath.replace(".pdf","_compressed.pdf")
        data = {'newFileName': str}
        with open(str, "wb") as fp:
            writer.write(fp)
    return render(request, 'download.html', data)


def download(request):
    if os.path.exists(request.GET['downloadFile']):
        with open(request.GET['downloadFile'], 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename =' + os.path.basename(request.GET['downloadFile'])
            return  response
    return render(request, 'split.html')