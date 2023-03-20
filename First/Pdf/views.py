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

def splitFile(request):
    if request.method == 'POST':
        file = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        filePath = fs.url(filename)
        reader = PdfReader("Data+Structures+and+Algorithms+Bootcamp+in+Python+slides+Remaster.pdf")
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.add_metadata(reader.metadata)

        with open("smaller-new-file.pdf", "wb") as fp:
            writer.write(fp)
    return render(request, 'split.html')