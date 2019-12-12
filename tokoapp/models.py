from django.db import models

# Create your models here.
class Barang(models.Model):
    nama_barang = models.CharField(max_length=200)
    harga = models.BigIntegerField(default=0)
    foto = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.nama_barang

class Deskripsi(models.Model):
    id_barang = models.ForeignKey(Barang, on_delete=models.CASCADE)
    deskripsi_barang = models.CharField(max_length=255)

    def __str__(self):
        return self.deskripsi_barang