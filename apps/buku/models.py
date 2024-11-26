from django.db import models

# Create your models here.
class Buku(models.Model):
    id = models.BigAutoField(primary_key=True)
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    tahun_terbit = models.IntegerField()
    isbn = models.CharField(max_length=20)
    kategori = models.CharField(max_length=50)
    deskripsi = models.TextField()
    cover = models.ImageField(upload_to='covers')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul
class Sampul(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField(max_length=225)

    def __str__(self):
        return self.name