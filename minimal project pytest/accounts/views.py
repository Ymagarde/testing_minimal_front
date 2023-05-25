
from email.policy import HTTP
from django.shortcuts import redirect
from pkg_resources import to_filename
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status, views, permissions

from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from rest_framework.authtoken.models import Token
from .serializers import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,parser_classes
from rest_framework import generics ,response
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser ,JSONParser
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
import uuid
import boto3
from django_filters.rest_framework import DjangoFilterBackend,OrderingFilter
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .helper import send_forget_password_mail
from django.contrib.auth import get_user_model
User = get_user_model()
from django_filters.rest_framework import DjangoFilterBackend


# Register API  with this Api user can Create their Account 
@method_decorator(csrf_exempt, name='dispatch')
class Register(APIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
            table = ddb.Table('Register')
            table.put_item(
                Item=serializer.data
            ) 
            user = User.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response( {'id':str(user.id),'refresh': str(refresh),'access': str(refresh.access_token),'message':"Register successfully"},status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login API  with this Api user can log into their Account
@method_decorator(csrf_exempt, name='dispatch')
class Login(APIView):
    serializer_class = LoginSerializer
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response( {'user':str(user.id),'refresh': str(refresh),'access': str(refresh.access_token),'message':"login successfully"})
        return response.Response({'message': "Invalid credentials, try again"}, status=status.HTTP_401_UNAUTHORIZED)
 


@method_decorator(csrf_exempt, name='dispatch')
class ChangePassword(APIView):
    parser_classes=[JSONParser]
    serializer_class = Reset_password_serializer
    def post(self,request,token):
        profile_obj = User.objects.get(forget_password_token = token)
        print(profile_obj)
        users_id = profile_obj.id
        print(users_id)
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        new_password=serializer.initial_data.get('new_password')
        print(new_password)
        user_obj = CustomUser.objects.get(id = users_id)
        user_obj.set_password(new_password)
        user_obj.save()
        return response.Response({'message': "Password change successfully now login"},status=status.HTTP_205_RESET_CONTENT)  

# Forget_password Api with this api user can share change password link to their associate mail id by entering thier username
@method_decorator(csrf_exempt, name='dispatch')
class Forget_password(APIView):
    parser_classes=[JSONParser]
    serializer_class = forget_password_serializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        email=serializer.initial_data.get('email')
        print(email)
        if not CustomUser.objects.filter(email = email).first():
            messages.success(request,'No User found with this username')
            return response.Response({'message': "No User found with this email"},status=status.HTTP_404_NOT_FOUND)
                
        user_obj=User.objects.get(email=email)
        token= str(uuid.uuid4())
        profile_obj=User.objects.get(username = user_obj)
        profile_obj.forget_password_token= token 
        profile_obj.save()
        send_forget_password_mail(user_obj.email, token )
        messages.success(request,'Reset Password Email has been sent to your Email ID')
        return response.Response({'message': "Reset Password Email has been sent to your Email ID"},status=status.HTTP_202_ACCEPTED)

        

# User_post api with this user can Post their photos or file with description
@method_decorator(csrf_exempt, name='dispatch')
class User_Post(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request,*args, **kwargs):
        #file_serializer = User_Post_serializer(data=request.data)
        file_serializer = User_Post_serializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
            table = ddb.Table('Posts')
            table.put_item(
                Item=file_serializer.data
            ) 
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#view post Api with this we can see different User's posts

class Post_view(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    queryset = Post.objects.filter(is_approved=True).order_by('-created_date')
    serializer_class = User_Post_get_serializer

@method_decorator(csrf_exempt, name='dispatch')
class Post_view_user(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = User_Post_get_serializer
    def get(self,request):
        accounts = Post.objects.filter(user = request.user).order_by('-created_date')
        serializer =User_Post_serializer(accounts , many = True) 
        return Response(serializer.data)
         

@method_decorator(csrf_exempt, name='dispatch')
class Post_update(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):  
        try:              
            ac =Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Response(status=404)   
        serializer = User_Post_serializer(ac) 
        return Response(serializer.data) 
    def put(self,request ,pk): 
        try:              
            ac = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
           return Response(status=404)  
        serializer = User_Post_serializer(ac , data = request.data )   
        if  serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)          
        else:
            return Response(serializer.errors)  
        
# User_Social Api with this Api we can Post User's Social Media URL's
@method_decorator(csrf_exempt, name='dispatch')
class User_Social(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Social.objects.all()
    serializer_class = Social_serializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
            table = ddb.Table('Socials')
            table.put_item(
                Item=serializer.data
            ) 
            return Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class User_Social_view(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self , request):
    accounts = Social.objects.filter(user = request.user) 
    serializer = Social_serializer(accounts , many = True) 
    return Response(serializer.data)    


@method_decorator(csrf_exempt, name='dispatch')
class User_Social_Update(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):  
        try:              
          ac = Social.objects.get(user=request.user)
        except Social.DoesNotExist:
          return Response(status=404)   
        serializer = Social_serializer(ac) 
        return Response(serializer.data) 
    def put(self,request): 
      try:              
        ac = Social.objects.get(user=request.user)
      except Social.DoesNotExist:
        return Response(status=404)  
      serializer = Social_serializer(ac , data = request.data )   
      if  serializer.is_valid():
        serializer.save()
        return Response("edit successfully")          
      else:
        return Response(serializer.errors)  

# User_About Api with this Api we can Post User's Social 


@method_decorator(csrf_exempt, name='dispatch')
class User_About(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = About.objects.all()
    serializer_class = About_serializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
            table = ddb.Table('about')
            table.put_item(
                Item=serializer.data
            ) 
            return Response(serializer.data)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    

class User_About_View(APIView):
  authentication_classes = [JWTAuthentication]
  permission_classes = [IsAuthenticated]
  def get(self , request):
    accounts = About.objects.filter(user = request.user) 
    serializer = About_serializer(accounts , many = True) 
    return Response(serializer.data)    

@method_decorator(csrf_exempt, name='dispatch')
class User_About_Update(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):  
      try:              
        ac = About.objects.get(user =request.user)
      except About.DoesNotExist:
        return Response(status=404)   
      serializer = About_serializer(ac) 
      return Response(serializer.data)
    def put(self,request): 
        try:              
            ac = About.objects.get(user =request.user)
        except About.DoesNotExist:
           return Response(status=404)  
        serializer =About_serializer(ac , data = request.data )   
        if  serializer.is_valid():
            serializer.save()
            return response.Response({'message': "Your About section update successfully"},status=status.HTTP_205_RESET_CONTENT)         
        else:
            return Response(serializer.errors) 


# User_Profile_Pic API with this API User can upload their Profile pic and Background Image
@method_decorator(csrf_exempt, name='dispatch')
class User_Profile_Pic(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    def get(self , request):
        accounts = Profile_Pic.objects.filter(user = request.user) 
        serializer = Profile_Pic_serializer(accounts , many = True) 
        return Response(serializer.data)    
    def post(self, request):
        file_serializer =Profile_Pic_serializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
            table = ddb.Table('Profile_pics')
            table.put_item(
                Item=file_serializer.data
            ) 
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(csrf_exempt, name='dispatch')
class User_Profile_pic_Update(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):  
        try:              
         ac = Profile_Pic.objects.get(user = request.user)
        except Profile_Pic.DoesNotExist:
          return Response(status=404)   
        serializer =  Profile_Pic_serializer(ac) 
        return Response(serializer.data) 
    def put(self,request ): 
      try:              
       ac = Profile_Pic.objects.get(user = request.user)
      except Profile_Pic.DoesNotExist:
        return Response(status=404)  
      serializer = Profile_Pic_serializer(ac , data = request.data )   
      if  serializer.is_valid():
        serializer.save()
        return Response("edit successfully " )          
      else:
        return Response(serializer.errors)  
   
@csrf_exempt
@api_view(['POST','GET'])
def Like_Post(request,id):
    post = Post.objects.filter(id = id)
    if request.user in post[0].liked_by.all():
       post[0].liked_by.remove(request.user)
    else:
        post[0].liked_by.add(request.user)
    return response.Response(status=status.HTTP_202_ACCEPTED) 


# User_Comment with this API user can comment on other user's post 
class CommentsViewSet(APIView):
    def get(self, request):
        com = Comments.objects.all()
        serializer = CommentsSerializer(com , many = True)
        return Response(serializer.data)  
    def post(self , request):
      file_serializer = CommentsSerializer1(data=request.data) 
      if file_serializer.is_valid():
        file_serializer.save()
        ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
        table = ddb.Table('Comments')
        table.put_item(
            Item=file_serializer.data
            ) 
        return Response(file_serializer.data)
      return response.Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
@api_view(['DELETE'])
def Comments_delete(request,pk):
      x = Comments.objects.get(cid = pk)
      x.delete()
      return Response("Comments is successfully delete")

# User_replay with this API user can comment on other user's post
class ReplyViewSet(APIView):
    def get(self, request):
       if request.method =='GET':
        social = Reply.objects.all()
        serializer = ReplySerializer1(social , many = True)
        return Response(serializer.data) 
    def post(self , request) :
      file_serializer = ReplySerializer(data=request.data) 
      if file_serializer.is_valid():              
        file_serializer.save()
        ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
        table = ddb.Table('Reply')
        table.put_item(
            Item=file_serializer.data
            ) 
        return Response(file_serializer.data)
      return response.Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def reply_delete(request,pk):
      x = Reply.objects.get(rid = pk)
      x.delete()
      return Response("Reply  is successfully delete")

# PostDetail with this API user can see Detailed view of any Post
class PostDetail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):  
      try:              
        ac = Post.objects.get(pk=pk)
      except Post.DoesNotExist:
        return Response(status=404)   
      serializer = User_Post_get_serializer(ac) 
      return Response(serializer.data)

# Blog viewset with this API user can post their blogs 
@method_decorator(csrf_exempt, name='dispatch')
class BlogPost(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser,JSONParser)
    def post(self , request) :
        serializer = BlogSerializer(data=request.data) 
        if serializer.is_valid():              
            serializer.save()  
            ddb = boto3.resource('dynamodb', 
                     aws_access_key_id='AKIA6GFBKQFECVUSCAHY', 
                     aws_secret_access_key='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',
                     region_name ='us-west-2')
            table = ddb.Table('Blog')
            table.put_item(
            Item=serializer.data
            ) 
            return Response(serializer.data)  
        else:
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)  
  

# Blog viewset with this API user can edit their blogs 
@method_decorator(csrf_exempt, name='dispatch')
class Blog_update(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):  
      try:              
        ac = Blog.objects.get(pk=pk)
      except Blog.DoesNotExist:
        return Response(status=404)   
      serializer = BlogSerializer(ac) 
      return Response(serializer.data)
    def put(self,request ,pk): 
        blog = Blog.objects.get(id=pk)
        serializer = BlogSerializer(instance=blog, data =request.data)
        if serializer.is_valid():
            serializer.save() 
        return response.Response({'message': "Your blog update successfully"},status=status.HTTP_205_RESET_CONTENT)



class Blog_view(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Blog.objects.all().order_by('-blog_name')
    serializer_class = BlogSerializer

# Blog viewset with this API user can delete their blogs 

class Blog_delete(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:   
            blog = Blog.objects.get(id=pk)
            blog.delete()
            return response.Response({'message': "Your blog delete successfully"},status=status.HTTP_205_RESET_CONTENT)
        except Blog.DoesNotExist:
            return Response("blog does not excite") 



#Blog viewset with this API user can blog Search Category  their blogs 
class CategoryListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog_name']
    Search_fields = ['Category']
  


@api_view(['GET'])
def show(request):
      if request.method =='GET':
        print(request.user)
        user = CustomUser.objects.filter(username=request.user)
        serializer = RegisterSerializer(user,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def video(request,pk):
      if request.method =='GET':
        user = Video.objects.filter(pk=pk)
        serializer = Videoserializer(user,many=True)
        return Response(serializer.data)
       
@api_view(['GET'])
def View_all_Posts(request):
      if request.method =='GET':
        post = Post.objects.filter(is_approved=True).order_by('-created_date')
        serializer = User_Post_get_serializer(post,many=True)
        return Response(serializer.data)



class Profile_data(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,pk):
        usr = Profile_Pic.objects.get(pk=pk)
        serializer = Profile_Pic_serializer(usr)
        return Response(serializer.data)
    
    
class About_data(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,pk):
        usr = About.objects.get(pk=pk)
        serializer = About_serializer(usr)
        return Response(serializer.data)
    
    
class social_data(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request,pk):
        usr = Social.objects.get(pk=pk)
        serializer = Social_serializer(usr)
        return Response(serializer.data)

class Post_data(APIView):
    def get(self, request,pk):
        user = Post.objects.get(user=pk)
        serializer = User_Post_get_serializer(user)
        return Response(serializer.data)  


#https://github.com/CryceTruly/django-rest-api/tree/main/authentication