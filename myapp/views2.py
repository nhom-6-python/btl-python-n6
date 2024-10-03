from django.shortcuts import render, redirect

# phuc

def index(request):
	n=0
	return render(request, 'index.html')