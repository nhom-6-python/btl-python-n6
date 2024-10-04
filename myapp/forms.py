from django import forms
from .models import Truyen, Chap, Trang, Thongbao, Nguoidung

class TruyenForm(forms.ModelForm):
	class Meta:
		model = Truyen
		fields = ["ten", "theloai", "mota", "tacgia", "anhbia", "anhnen"]