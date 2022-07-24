from django.db import models


# Create your models here.
class Serial(models.Model):
    code = models.IntegerField(default=None)

    def __str__(self):
        return str(self.code)


class UserOn(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    password=models.CharField(max_length=100,null=False,blank=False,default='')
    company = models.CharField(max_length=80)
    email = models.EmailField(max_length=60)
    serial = models.OneToOneField(Serial,on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + " " + self.last_name


class User(models.Model):
    first_name = models.CharField(max_length=60,null=False,blank=False,default=None)
    last_name = models.CharField(max_length=60,null=False,blank=False,default=None)
    company = models.CharField(max_length=60,null=False,blank=False,default=None)
    email = models.CharField(max_length=60,null=False,blank=False,default=None)
    password=models.CharField(max_length=60,null=False,blank=False,default=None)
    def __str__(self):
        return str(self.id)




class Product(models.Model):
    name = models.CharField(max_length=150)
    disc=models.CharField(max_length=150,null=False,blank=False, default='')
    picture = models.ImageField(null=True, blank=True, upload_to='images/')
    def __str__(self):
        return self.name
class Orders(models.Model):
    state = models.BooleanField(default=False)
    UNITS= [
        ('kg', 'kg'),
        ('tone', 'tone'),
        ('kuntal', 'kuntal'),
    ]
    TIMES=[('once','Only once'),('week','Every week'),('month','Every month'),]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField(default=10)
    unit = models.CharField(max_length=50,choices=UNITS,default='kg')
    for_when = models.DateField('when to deliver')
    how_many_times=models.CharField('How many time to deliver',max_length=70,choices=TIMES,default='Every week')

class Advertisement(models.Model):
    Title = models.CharField(max_length=40)
    description = models.CharField(max_length=1200)
    video = models.URLField(max_length=1200)
    def __str__(self):
        return self.Title + " " + self.description




class FromComp(models.Model):
    post = models.TextField(max_length=1200,default="")


class Setting(models.Model):
    name = models.CharField(max_length=40)
    state = models.BooleanField()


class CommentsP(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=1000)
    url = models.URLField(null=True, blank=True)


class CommentsB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=False)
    comment = models.CharField(max_length=1000)
class PostLink(models.Model):
    post=models.ForeignKey(FromComp,on_delete=models.CASCADE)
    index=models.CharField(max_length=455,default='Post')
class link(models.Model):
    post=models.ForeignKey(PostLink,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,null=False,blank=False,default='click here')
    url=models.URLField(max_length=999999999,null=False,blank=False,default='')





