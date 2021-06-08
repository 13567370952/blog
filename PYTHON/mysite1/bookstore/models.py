from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(verbose_name='书名',max_length=50,default='')
    price = models.DecimalField('价格',max_digits=7,decimal_places=2)
    info = models.CharField('描述',max_length=100,default='')

    # class Meta:
    #     db_table = 'book'
    def __str__(self):
        return '%s|%s|%s'(self.title,self.price,self.info)

class Author(models.Model):
    name = models.CharField('姓名',max_length=11,default='')
    age = models.IntegerField('年龄')
    email = models.EmailField('邮箱')