from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Comment(models.Model):
#    post = models.ForeignKey(Post,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.name


class OtherIf(models.Model):
    name=models.CharField("姓名",max_length=20)
    phone=models.CharField("电话",max_length=20)
    numb = models.CharField("工号",max_length=20)
    service = models.CharField("负责业务",max_length=200)


class StaffIf(models.Model):
    name=models.CharField("姓名",max_length=20)
    phone=models.CharField("电话号码",max_length=20)
    mail = models.EmailField("邮箱")
    incomp = models.CharField("今天是否上班",max_length=2,choices=(("上班","上班"),("休息","休息")))   
    service = models.TextField("负责业务")
    work = models.TextField("工作安排")
    
    class Meta:
        db_table = "EmInformation"
    def __str__(self):
        
        return(self.name)

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='发表')


class Post(models.Model):
    STATUS_CHOICES = (('草稿','草稿'),('发表','发表'))
    title = models.CharField('文章题目',max_length=250)
    slug = models.SlugField('url',max_length=250,unique_for_date='publish')
#    author = models.ForeignKey(User,related_name='blog_posts',verbose_name="作者")
    author=models.CharField("作者",max_length=20)
    body = models.TextField("文章内容")
    publish = models.DateTimeField('创作时间',default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True)
    status = models.CharField("是否发表",max_length=10,choices=STATUS_CHOICES,default='草稿')
    
    class Meta:
        ordering = ('-publish',)
      
    def __str__(self):
          
        return(self.title)
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.strftime('%m'),
                                                self.publish.strftime('%d'),
                                                self.slug])

    objects = models.Manager()
    published = PublishedManager()






