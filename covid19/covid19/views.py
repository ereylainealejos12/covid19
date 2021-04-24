from django.shortcuts import render

def home(request):

    return render(request, 'covid19/tracker.html')
