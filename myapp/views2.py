from django.shortcuts import render, redirect

# phuc

def index(request):

	return render(request, 'index.html')