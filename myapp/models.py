from django.db import models

# Create your models here.

class Truyen(models.Model):
	ten = models.CharField(max_length=255)
	theloai = models.TextField()
	mota = models.TextField()
	tacgia = models.CharField(max_length=255)
	luotthich = models.BigIntegerField(default=0)
	anhbia = models.FileField(upload_to='anhbia/', blank=True)
	anhnen = models.FileField(upload_to='anhnen/', blank=True)
	@property
	def luotxem(self):
		return sum(x.luotxem for x in self.chap.all())
	
	
class Chap(models.Model):
	stt = models.FloatField(default=0)
	ten = models.CharField(max_length=255)
	luotxem = models.BigIntegerField(default=0)
	thoigiandang = models.DateTimeField(auto_now_add=True)
	truyen = models.ForeignKey(Truyen, on_delete=models.CASCADE, related_name='chap', blank=True, null=True, default=0)

class Trang(models.Model):
	anh = models.FileField(upload_to='anhchap/')
	chap = models.ForeignKey(Chap, on_delete=models.CASCADE, related_name='chap', blank=True, null=True, default=0)

class Thongbao(models.Model):
	noidung = models.CharField(max_length=255)

class Nguoidung(models.Model):
	ten = models.CharField(max_length=255)
	matkhau = models.CharField(max_length=255)
	vaitro = models.CharField(max_length=255)
	yeuthich = models.ManyToManyField(Truyen, related_name='yeuthich', blank=True)
	lichsu = models.ManyToManyField(Truyen, related_name='lichsu', blank=True)
	thongbao = models.ManyToManyField(Thongbao, related_name='thongbao', blank=True)
	truyendang = models.ManyToManyField(Truyen, related_name='truyendang', blank=True)
	@property
	def luotxem(self):
		return sum(x.luotxem for x in self.truyendang.all())
