from django.shortcuts import render
from django.http import HttpResponse
from .models import Apply

# Create your views here.
def apply(request):
    if request.method == 'POST':
        apply_inst = Apply()
        apply_inst.applicant_name = request.POST['character_name']
        apply_inst.applicant_email = request.POST['email']
        apply_inst.applicant_age = request.POST['age']
        apply_inst.applicant_favmmo = request.POST['favoritemmo']
        apply_inst.about_you = request.POST['about_you']
        apply_inst.save()
        return HttpResponse("Application submitted")
    else:
        return render(request, 'apply/apply.html')
