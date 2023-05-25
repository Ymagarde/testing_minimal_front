from statistics import mode
from django.db import models
from email_login import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from mptt.models import MPTTModel, TreeForeignKey 

# Create your models here.

class CustomUser(AbstractUser):
    
    email = models.EmailField(_('email address'), unique=True)
    number =models.CharField(max_length=20,null=True,blank=True)
    forget_password_token= models.CharField(max_length=100)
   


class Blog(models.Model):
    tag_name = models.CharField(max_length=100,default='')
    blog_name = models.CharField(max_length=200,default='')
    created_date = models.DateTimeField(default=now)
    update_date =models.DateTimeField(auto_now_add=now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    images= models.ImageField(upload_to='images/',null = True,blank =True)
    is_approved = models.BooleanField(default=False)
    def __str__(self):
        return self.blog_name[0:20]+'....'+'by '+self.user.email

class Profile_Pic(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='user')
    background_image = models.ImageField(upload_to='images/',null = True,blank = True)
    images= models.ImageField(upload_to='images/',null = True,blank =True)

    @property
    def imageURL(self):
        try:
            url = self.images.url 
        except:
            url = ''
        return url 
    @property
    def backgroundURL(self):
        try:
            url = self.backgound_image.url
        except:
            url =''
        return url

class Post(models.Model):
    post_name =models.CharField(max_length=100,default='')
    tag_name = models.CharField(max_length=100,default='')
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    post_header= models.CharField(max_length=500,default='')
    post_content= models.CharField(max_length=500,default='')
    images= models.ImageField(upload_to='images/',blank =True)
    document =models.FileField(upload_to='File/',blank =True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='likes',blank=True)
    created_date = models.DateTimeField(default=now)
    update_date = models.DateTimeField(auto_now_add=now)
    is_active = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='userss')
    
    def __str__(self):
        return self.user

    def __str__(self):
        return self.post_name[0:10]+'...'+'by'+ self.user.email
    
    @property
    def imageURL(self):
        try:
            url = self.images.url
        except:
            url = ''
        return url

    @property
    def documentURL(self):
        try:
            url = self.document.url
        except:
            url = ''
        return url

class Comments(models.Model): 
       
    cid = models.AutoField(auto_created=True,primary_key=True)
    text = models.CharField(max_length=500)
    #parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='children')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    Post =  models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    
    # class MPTTMeta:
    #     order_insertion_by = ['datetime']
    
    def __str__(self):
        return f'Comment by {self.name}'
    def __str__(self):
        return str(self.text)

class Reply(MPTTModel):
       
    rid = models.AutoField(auto_created=True,primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Comments =  models.ForeignKey(Comments,on_delete=models.CASCADE,related_name='reply')
    parent = TreeForeignKey('self',on_delete=models.CASCADE,null=True, blank=True, related_name='children') 
    content =  models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    
    class MPTTMeta:
        order_insertion_by = ['datetime']
    
    def __str__(self):
        return f'Reply by {self.name}'
    def __str__(self):
        return str(self.content)
    def __str__(self):
        return self.content[0:10]+'...'+'by '+ self.user.email


class Social(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    linkedin = models.URLField(max_length=500,null=True,blank=True)
    twitter= models.URLField(max_length=500,null=True,blank=True)
    instagram = models.URLField(max_length=500,null=True,blank=True)
    facebook = models.URLField(max_length=500,null=True,blank=True)
      
    def __str__(self):
        return self.user.email

class About(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,primary_key=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    location = models.CharField(max_length=100,null=True,blank=True)
    email= models.EmailField(max_length=100,null=True,blank=True)
    workad_at = models.CharField(max_length=100,null=True,blank=True)
    Studied_at = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.user.email
        
class change_password(models.Model):
    new_password = models.CharField(max_length=500)
    confirm_password = models.CharField(max_length=500)


class Video(models.Model):
    video = models.video = models.FileField(upload_to='videos_uploaded',null=True)
    
