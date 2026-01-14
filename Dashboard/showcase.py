from django.shortcuts import render
from FrontendDev.models import FrontEndTeam
from BackendDev.models import BackEndTeam
from OnlineBatchTeam.models import OnlineBatchMentor
from Editorteam.models import EditorTeam

def EmpDashboard(request):
    frontendteam = FrontEndTeam.objects.all()
    backendteam = BackEndTeam.objects.all()
    onlinebatchteam = OnlineBatchMentor.objects.all()
    editorteam = EditorTeam.objects.all()
    context = {
        'Frontend_info': frontendteam,
        'Backend_info': backendteam,
        'OnlineBatch_info': onlinebatchteam,
        'EditorTeam_info' : editorteam
    }
    return render(request, 'index.html', context )