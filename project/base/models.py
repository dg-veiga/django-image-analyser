from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
        
    class Meta:
        db_table = "base_image"

class Analysis(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
        
    class Meta:
        db_table = "base_analysis"