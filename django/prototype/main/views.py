from django.shortcuts import render
from django.http import HttpResponse

# Create View

def homepage(request):
	return render(request, "login.html", {});

