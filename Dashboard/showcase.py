from django.shortcuts import render
from FrontendDev.models import FrontEndTeam
from BackendDev.models import BackEndTeam

def EmpDashboard(request):
    frontendteam = FrontEndTeam.objects.all()
    backendteam = BackEndTeam.objects.all()
    context = {
        'Frontend_info': frontendteam,
        'Backend_info': backendteam
    }
    return render(request, 'index.html', context )