from django.shortcuts import render, get_object_or_404
from .models import OnlineBatchMentor

# Create your views here.
def onlinebatchteam(request, pk):
    OnlineBatch_Details = get_object_or_404(OnlineBatchMentor, pk=pk)
    context = {
        'OnlineBatch_info': OnlineBatch_Details
    }

    return render(request, 'OnlineBatchTeam.html', context)