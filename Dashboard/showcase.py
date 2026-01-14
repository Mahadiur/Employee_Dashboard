from django.shortcuts import render

def EmpDashboard(request):
    return render(request, 'index.html')