from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'testingapp/home.html')

def pictures(request):
    return render(request,'testingapp/pictures.html')
