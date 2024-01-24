from django.shortcuts import render
from .forms import RegistrationForm
from django.http import HttpResponseRedirect
def index(request):
	return render(request, 'pages/home.html')
def contact(request):
	return render(request, 'pages/contact.html')
def custom_404(request, exception=None):
    return render(request, 'pages/404.html', status=404)
def custom_500(request, exception=None):
    return render(request, 'pages/500.html', status=500)
def register(request):
	form = RegistrationForm()
	if request.method == 'POST':
		form= RegistrationForm(request.POST)
		if form.is_valid():
			form.Save()
			return HttpResponseRedirect('/')

	return render(request, 'pages/register.html', {'form':form})

# Create your views here.
