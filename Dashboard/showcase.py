from django.shortcuts import render
from FrontendDev.models import FrontEndTeam
from BackendDev.models import BackEndTeam
from OnlineBatchTeam.models import OnlineBatchMentor

def EmpDashboard(request):
    frontendteam = FrontEndTeam.objects.all()
    backendteam = BackEndTeam.objects.all()
    onlinebatchteam = OnlineBatchMentor.objects.all()
    context = {
        'Frontend_info': frontendteam,
        'Backend_info': backendteam,
        'OnlineBatch_info': onlinebatchteam
    }
    return render(request, 'index.html', context )