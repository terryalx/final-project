from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=2000)
    author = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=99999999, default='No description available')
    image = models.ImageField(upload_to='blogpost/%Y/%m/%d')
    tag = models.CharField(max_length=100)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.title} - {self.tag}'
    
class BookStore(models.Model):
    image = models.ImageField(upload_to='bookstore/%Y/%m/%d')
    title = models.CharField(max_length=2000)
    author = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=99999999, default='No description available')
    tag = models.CharField(max_length=100)
    link = models.CharField(max_length=100, blank=True)
    # add ratings
    # price
    # add best seller
    
    def __str__(self):
        return f'{self.title} - {self.tag}'
