from django.shortcuts import render

# Create your views here.
def defender(request):
    return render(request,'defender.html')