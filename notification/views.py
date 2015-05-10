from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
	c={ }
	c.update(csrf(request))
	return render('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
	return render('loggedin,html')

def invalid_login(request):
	return render('invalid_login.html')

def logout(request):
	auth.logout(request)
	return render('logout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
        
    else:
        form = UserCreationForm()
    	args = {}
    	args.update(csrf(request))
    
    	args['form'] = form
    	return render('register.html', args)



def register_success(request):
    return render('register_success.html')