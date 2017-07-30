from django.shortcuts import render
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login


# Create your views here.
def user_login(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'accounts/login.html', {'error': 'Login Successful!'})
        else:
            return render(request, 'accounts/login.html', {'error': 'The username and or password was incorrect'})
    else:
        return render(request, 'accounts/login.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['name'])
                return render(request, 'accounts/signup.html', {'error': 'Username ' + request.POST['name'] + ' already in use'})
            except User.DoesNotExist:
                 User.objects.create_user(request.POST['name'], password=request.POST['password1'])
                 user = User.objects.get(username=request.POST['name'])
                 public_group = Group.objects.get(name='Public')
                 user.groups.add(public_group)
                 login(request, user)
                 return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords did not match'})
    else:
        return render(request, 'accounts/signup.html')


