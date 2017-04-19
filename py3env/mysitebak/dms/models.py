from django.db import models

# Create your models here.

class User(models.Model):
    YN = (('N','NO'),('Y','YES'))
    name = models.CharField("姓名",max_length=30)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    passwd = models.CharField("密码",max_length=128)
    email=models.EmailField()
    job_number = models.CharField("工号",max_length=10,unique=True)
    is_staff = models.CharField("是否是员工",max_length=1,choices=YN,default='Y')
    is_active = models.CharField("是否激活",max_length=1,choices=YN,default='N')
    is_superuser = models.CharField("是否是超级用户",max_length=1,choices=YN,default='N')
    last_login = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name



class AuthUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username


