from django.db import models

# Create your models here.

class Truyen(models.Model):
	ten = models.CharField(max_length=255)
	theloai = models.TextField()
	mota = models.TextField()
	tacgia = models.CharField(max_length=255)
	luotthich = models.BigIntegerField(default=0)
	@property
	def luotxem(self):
		return sum(x.luotxem for x in self.chap.all())
	
	
class Chap(models.Model):
	ten = models.CharField(max_length=255)
	luotxem = models.BigIntegerField(default=0)
	thoigiandang = models.DateTimeField(auto_now_add=True)
	Truyen = models.ForeignKey(Truyen, on_delete=models.CASCADE, related_name='chap')

class Thongbao(models.Model):
	chap = models.CharField(max_length=255)

class Nguoidung(models.Model):
	ten = models.CharField(max_length=255)
	matkhau = models.CharField(max_length=255)
	vaitro = models.CharField(max_length=255)
	yeuthich = models.ManyToManyField(Truyen, related_name='yeuthich')
	lichsu = models.ManyToManyField(Truyen, related_name='lichsu')
	thongbao = models.ManyToManyField(Thongbao, related_name='thongbao')
	truyendang = models.ManyToManyField(Truyen, related_name='truyendang')
	@property
	def luotxem(self):
		return sum(x.luotxem for x in self.truyendang.all())
			
