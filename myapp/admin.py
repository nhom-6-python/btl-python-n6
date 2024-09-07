from django.contrib import admin
from .models import Truyen, Chap, Thongbao, Nguoidung
# Register your models here.

class TruyenAdmin(admin.ModelAdmin):
	list_display = ("id", "ten", "theloai", "mota", "tacgia", "luotthich", "luotxem")

class ChapAdmin(admin.ModelAdmin):
	list_display = ("id", "ten", "luotxem", "thoigiandang", "Truyen")

class ThongbaoAdmin(admin.ModelAdmin):
	list_display = ('id','chap')

class NguoidungAdmin(admin.ModelAdmin):
	list_display = ('ten', 'matkhau', 'vaitro', 'luotxem')

admin.site.register(Truyen, TruyenAdmin)
admin.site.register(Chap, ChapAdmin)
admin.site.register(Thongbao, ThongbaoAdmin)
admin.site.register(Nguoidung, NguoidungAdmin)