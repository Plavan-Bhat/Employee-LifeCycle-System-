from django.shortcuts import render, redirect
from .forms import CandidateForm
from .models import Candidate

def interview_dashboard(request):
    candidates = Candidate.objects.all()
    return render(request, 'interview/dashboard.html', {'candidates': candidates})

def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interview_dashboard')
    else:
        form = CandidateForm()
    return render(request, 'interview/add_candidate.html', {'form': form})
