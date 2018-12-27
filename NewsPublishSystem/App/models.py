from django.db import models

# Create your models here.

class User(models.Model):
    uid=models.CharField(primary_key=True,max_length=20)
    username=models.CharField(max_length=20,unique=True)
    password=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)
    email=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    idNumber=models.CharField(max_length=20)
    userToken=models.CharField(max_length=20) #用於判斷是否在線
    
    @classmethod
    def createUser(cls,Uid,Name,Passwd,Phone,Email,Country,Idnumber,Usertoken):
        u=cls(uid=Uid,username=Name,password=Passwd,phone=Phone,email=Email,country=Country,idNumber=Idnumber,userToken=Usertoken)
        return u

    class Meta:
        db_table="user"

class New(models.Model):
    nid=models.IntegerField(primary_key=True)
    # headLine=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    content=models.CharField(max_length=500)
    commentNumber=models.IntegerField()
    publishTime=models.DateField()
    # author=models.DateField(max_length=20) #文章发布时间
    articleAuthor=models.CharField(max_length=20)#文章作者
    readerNumber=models.IntegerField()
    country=models.CharField(max_length=20)
    continent=models.CharField(max_length=10)

    class Meta:
        db_table='new'

class Admin(models.Model):
    aid=models.IntegerField(primary_key=True)
    adminName=models.CharField(max_length=10,unique=True)
    password=models.CharField(max_length=20)

    class Meta:
        db_table='admin'


class Comment(models.Model):
    content=models.CharField(max_length=50)
    cTime=models.DateField()
    publishAuthor=models.CharField(max_length=20,primary_key=True)

    class Meta:
        db_table='comment'