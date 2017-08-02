from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
        subject = "Insanity Rising application confirmation"
        message = "This email is a Confirmation of your application being submitted. \nThanks, \nThe Insanity Rising Team."
        apply_inst.send_conf_email(subject, message, "support@insanityrising.com", request.POST['email'])
        return HttpResponseRedirect("Application submitted")
    else:
        return render(request, 'apply/apply.html')
