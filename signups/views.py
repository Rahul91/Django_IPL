from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
#from django.template.loader import get_template
#from django.template import Context
from models import signup
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from models import ipl_scores 
#from forms import customizedform

def login(request):
	c={ }
	c.update(csrf(request))
	#c['id']=User.objects.get(username=uname)
	return render(request,'login.html')

def auth_view(request,id=1):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		a=str(User.objects.get(username=user.username).id)
		#a=''
		#for i in range(len(user.username)):
		#	a=a+user.username[i]
		
		return HttpResponseRedirect('/accounts/loggedin/'+(a))
		'''
		id=User.objects.get(id=1)
		args = {}
	 	args.update(csrf(request))
	 	return render(request,"loggedin.html", args)
'''
	else:
		return HttpResponseRedirect('/accounts/invalid')

def loggedin(request,id=1):
	#form = ipl_scores()
	args = {}
 	args.update(csrf(request))

 	#args['form'] = ipl_scores()
 	args['loggedin'] = True
 	args['get_id']=User.objects.get(id=id)
	return render(request,'loggedin_2.html',args)

def invalid_login(request):
	return render(request,'invalid_login.html')

def logout(request):
	auth.logout(request)
	return render(request,'logout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')
     	else:
     		return HttpResponseRedirect('/accounts/bad_request')
        
    else:
    	
        form = UserCreationForm()
    	args = {}
    	args.update(csrf(request))

    
    	args['form'] = UserCreationForm()
    	args['login'] = True

    	return render(request,'register.html', args)

	'''    args = {}
    args.update(csrf(request))
    args['email'] = signup.objects.all()
    return render(request,"signup.html", args)
'''

def register_success(request):
    return render(request,'register_success.html')

# Create your views here.

def home(request):
	args = {}
	args.update(csrf(request))

	args['email'] = signup.objects.all()
	return render(request,"signup.html", args)

def unsuscibe(request,id):
	#args={}
	#args.update(csrf(request))

	d=User.objects.get(id=id)
	d.delete()
	return HttpResponseRedirect('/')

def bad_request(request):
	return render(request, "bad_request.html")
