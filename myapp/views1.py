from django.shortcuts import render, redirect
from .forms import TruyenForm
# Create your views here.

def home(request):
	if request.method == 'POST':
		if 'upload-truyen' in request.POST:
			form = TruyenForm(request.POST, request.FILES)
			if form.is_valid():
				form.save()
				print('save')
				return redirect('/admin')
			else:
				print('save not done')
				return render(request, 'home.html', {'form': form})
	return render(request, 'home.html')