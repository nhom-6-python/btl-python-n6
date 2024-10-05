from django.shortcuts import render, redirect
from .models import Truyen, Chap, Trang, Thongbao, Nguoidung
from .forms import TruyenForm
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
# Create your views here.

def top3_by_like():
	top3 = Truyen.objects.all().order_by('-luotthich')[:3]
	return top3

def home(request):
	top3 = top3_by_like()
	context = {
		'top3' : top3
	}
	return render(request, 'home.html', context)

# def upload(request):
# 	if request.method == 'POST':
# 		if 'upload-truyen' in request.POST:
# 			form = TruyenForm(request.POST, request.FILES)
# 			if form.is_valid():
# 				form.save()
# 				print('save')
# 				return redirect('/admin')
# 			else:
# 				print('save not done')
# 				return render(request, 'home.html', {'form': form})
# 	return render(request, 'home.html')