from django.shortcuts import render

# Create your views here.
def interview_dashboard(request):
    return render(request, 'interview/dashboard.html')