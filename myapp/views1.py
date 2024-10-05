from django.shortcuts import render, redirect
from .models import Truyen, Chap, Trang, Thongbao, Nguoidung
from .forms import TruyenForm
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
# Create your views here.

# chức năng trang home

def top3_by_like(): # top 3 truyện có lượt yêu thích cao nhất( slider trang home)
	top3 = Truyen.objects.all().order_by('-luotthich')[:3]
	return top3

def new_update():
	chaps = Chap.objects.all().order_by('-thoigiandang')
	new_update = list()
	for x in chaps:
		if x.truyen not in new_update:
			new_update.append(x.truyen)
	new_update = new_update[:12]
	print(new_update)
	for x in new_update:
		print(x.ten)
	return new_update

def home(request): # view trang home
	list_new_update = new_update()
	top3 = top3_by_like()
	context = {
		'top3' : top3,
		'list_new_update': list_new_update
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