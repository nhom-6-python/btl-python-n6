from django.shortcuts import render, redirect
from .models import Truyen, Chap, Trang, Thongbao, Nguoidung
from .forms import TruyenForm
from datetime import datetime, timedelta
from django.utils.timezone import make_aware
from django.utils import timezone
from django.db.models import Sum,Q
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
	return new_update

def top_view(time): # lọc ra truyện nhiều view nhất trong tuần/tháng/all
	if time == 'tuan':
		today = datetime.today()
		start_of_week = today - timedelta(days=today.weekday())
		end_of_week = start_of_week + timedelta(days=6)
		top_view = (
			Truyen.objects
			.annotate(total_views=Sum('chap__luotxem', filter=Q(chap__thoigiandang__gte=start_of_week) & Q(chap__thoigiandang__lte=end_of_week)))
			.order_by('-total_views')[:10]  # Lấy 9 truyện có lượt xem cao nhất
		)
		return top_view

def home(request): # view trang home
	top3 = top3_by_like()
	list_new_update = new_update()
	list_top_view = top_view("tuan")
	cnt = 0
	list_top_view_row1 = list()
	list_top_view_row2 = list()
	list_top_view_row3 = list()

	for x in list_top_view:
		if cnt <=2:
			list_top_view_row1.append(x)
		elif cnt <=5:
			list_top_view_row2.append(x)
		else:
			list_top_view_row3.append(x)
		cnt+=1
	context = {
		'top3' : top3,
		'list_new_update': list_new_update,
		'list_top_view': list_top_view,
		'list_top_view_row1': list_top_view_row1,
		'list_top_view_row2': list_top_view_row2,
		'list_top_view_row3': list_top_view_row3,
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