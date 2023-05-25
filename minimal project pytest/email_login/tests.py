'''from rest_framework.test import APIRequestFactory
# Using the standard RequestFactory API to create a form POST request
factory = APIRequestFactory()
request = factory.post('/notes/', {'title': 'new idea'})
#import unittest
#from django import VERSION
from accounts.models import* 
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework import reverse
from django.contrib.auth import*
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
 


class login(APITestCase):
    def test_login1(self):
        email = "shivpawar@gmail.com"
        password = "123456"
        user = authenticate(username=email,password=password)
        if user:
            _response = self.clint.post('/login/',data=user)
            self.assertEqual(_response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(user['status'],True)
        print("POST Method status code for Success:",401) '''
'''class login(APITestCase):
    def test_login2(self):
        email = "shivpawar@gmail.com"
        password = ""
        user = authenticate(username=email,password=password)
        if user:
            
            _response = self.clint.post('/login/',data=user)
            return self.assertEqual(_response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(user['status'],False)
        print("POST Method status code for Failed:",401)
        return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)'''

'''class login(APITestCase):
    def test_login3(self):
        email = ""
        password = "123456"
        user = authenticate(username=email,password=password)
        if user:
            _response = self.clint.post('/login/',data=user)
            self.assertEqual(_response.status_code,status.HTTP_404_CREATED)
            self.assertEqual(user['status'],True)
        print("POST Method status code for Failed:",401)    
        
        return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)'''
'''class Register(APITestCase):
    def setUP1(self):
        Register.objects.create(
        email = "shivpawar@gmail.com",
        username = "shivpawar",
        password ="shivkumarpawar",
        first_name ="shiv",
        last_name = "pawar",
        number = "9589544515")
    def test_post_method(self):
        email = "shivpawar@gmail.com"
        password = "123456"
        username ="shivpawar"
        first_name ="shiv",
        last_name = "pawar",
        number = "9589544515"
        user = ""
        if user:
            response = self.client.post(format='json')
            self.assertEqual(response.status_code,401)
        print("POST Method status code for Success:",401)    
        return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)'''
        
        
'''class Register(APITestCase):
    def setUP2(self):
        self.ragister_url = ('/register/')
        Register.objects.create(
        email = "shivpawar@gmail.com",
        username = "shivpawar",
        password ="shivkumarpawar",
        first_name ="shiv",
        last_name = "pawar",
        number = "9589544515")
    def test_post_method1(self):
        url="http://127.0.0.1:8000/register/"
        data={'email' : "",
            'password' : "",
            'username' : "",
            'user' : ""
            }
        response = self.client.post(url,data,format="json")
        print("Register Method status code for fail:",response.status_code)
        self.assertEqual(response.status_code,400,False)'''
        
    
'''class ChangePassword(APITestCase):
    def test_ChangePassword1(self):
        email = "shivpawar@gmail.com"
        password = "123456"
        new_password = "121212"
        user = authenticate(username=email,password=password,new_password=new_password)
        if user:
            _response = self.clint.post('change-password/<token>/',data=user)
            self.assertEqual(_response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(user['status'],False)
        print("ChangePassword Method status code for Success:",404)
        return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)'''
        
'''class ChangePassword(APITestCase):
    def test_ChangePassword2(self):
        email = "shivpawar@gmail.com"
        password = "123456"
        new_password = "shiv"
        user = authenticate(username=email,password=password,new_password=new_password)
        if user:
            response = self.clint.post('change-password/id/',data=user)
            self.assertEqual(response.status_code, status.HTTP_404_CREATED)
            self.assertEqual(user['status'],False)
        print("ChangePassword Method status code for Failed:",404)    
        return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)'''

'''class ChangePassword(APITestCase):
    def test_ChangePassword2(self):
        email = "shivpawar@gmail.com"
        password = "123456"
        new_password = "shiv"
        user = authenticate(forget_password_token = 'token',id = 'users_id')
        if user:
            response = self.user.post('change-password/id/',data=user)
            self.assertEqual(response.status_code, status.HTTP_205_CREATED)
            self.assertEqual(user['status'],False)
        print("ChangePassword Method status code for  Success:",205)    
        return self.assertEqual(205,status.HTTP_205_RESET_CONTENT)'''
      
'''class ChangePassword(APITestCase):
    def test_ChangePassword2(self):
        email = "shivpawar@gmail.com"
        password = "123456"
        new_password = "shiv"
        user = authenticate(forget_password_token = 'token',id = 'users_id')
        if user:
            response = self.user.post('change-password/id/',data=user)
            self.assertEqual(response.status_code, status.HTTP_404_CREATED)
            self.assertEqual(user['status'],False)
        print("ChangePassword Method status code for  Success:",400)    
        return self.assertEqual(400,status.HTTP_400_BAD_REQUEST)'''
'''class Forget_password(APITestCase):
    def test_Forget_password1(self):
        email = "shivpawar@gmail.com"
        password = "123456"
        username = "shiv"
        new_password = "shiv123"
        user = authenticate(email=email,password=password,username=email,new_password=new_password)
        if user:
            _response = self.clint.post('forget_password/',data=user)
            self.assertEqual(_response.status_code, status.HTTP_404_CREATED)
            self.assertEqual(user['status'],False)
        print("Forget_password Method status code for Success:",status.HTTP_404_NOT_FOUND)'''
                

'''class Forget_password(APITestCase):
    def test_Forget_password2(self):
        data={'email' : "shivpawar@gmail.com",
        'password' : "123456",
        'username' : "123"
        }
        url = "http://127.0.0.1:8000/forget_password/"
        response = self.client.get(url, format='json')
        print("Forget_password Method status code for Failed:",404)    
        return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)

class Forget_password(APITestCase):
    def test_Forget_password2(self):
        data={'email' : "shivpawar@gmail.com",
        'password' : "123456",
        'username' : "123"
        }
        url = "http://127.0.0.1:8000/forget_password/"
        response = self.client.get(url, format='json')
        print("Forget_password Method status code for Failed:",404)    
        return self.assertEqual(404,status.HTTP_404_NOT_FOUND)'''
        
'''class User_Post(APITestCase):
    def setUP1(self):
        Post.objects.all(post_name = "googal",
        tag_name = "python",
        blog = "python",
        post_header = "python devloper",
        post_content = "fullstace devloper",
        user = "")
    def test_post_method(self):
        url="http://127.0.0.1:8000/user_post/"
        data={
            'post_name' : "googal",
            'tag_name' : "python",
            'blog' : "food",
            'post_header' : "python devloper",
            'post_content' : "googal is a most popular brouser",
            'images' : "",
            'document' : "",
            'likes' : "",
            'created_date' :"",
            'update_date'  : "",
            'user' : ""
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("POST Method status code for Success:",response.status_code)'''

'''class User_Post(APITestCase):
    def setUP2(self):
        Post.objects.all(post_name = "googal",
        tag_name = "python",
        blog = "python",
        post_header = "python devloper",
        post_content = "fullstace devloper",
        user = "")
    def test_post_method_success(self):
        url="http://127.0.0.1:8000/user_post/"
        
        post_name = "googal",
        tag_name = "python",
        blog = "food",
        post_header = "python devloper",
        post_content = "googal is a most popular brouser",
        images = "",
        document =  "",
        likes =  "",
        created_date  = "",
        update_date  = "",
        user = "" 
        if user :
            response = self.clint.post('user_post/')
            self.assertEqual(user['status'],True)
            #self.assertEqual(response.status_code,201)
        print("POST Method status code for Success:",response.status_code,201)
        self.assertEqual(response.status_code)
    def test_post_method_success(self):
        url="http://127.0.0.1:8000/user_post/"
        data={
            'post_name' : "googal",
            'tag_name' : "python",
            'blog' : "food",
            'post_header' : "python devloper",
            'post_content' : "googal is a most popular brouser",
            'images' : "",
            'document' : "",
            'likes' : "",
            'created_date' :"",
            'update_date'  : "",
            'user' : ""
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("POST Method status code for Success:",response.status_code)'''   

'''class Post_view(APITestCase):
    def user(self):
        Post.objects.create(
        email = "shivpawar@gmail.com",
        username = "shivpawar",
        password ="shivkumarpawar",
        first_name ="shiv",
        last_name = "pawar",
        number = "9589544515")

    def setUP(self):
        Post.objects.all(post_name = "googal",
        tag_name = "python",
        blog = "python",
        post_header = "python devloper",
        post_content = "fullstace devloper",
        user = 1)
    def test_get_method_success(self):
        url="http://127.0.0.1:8000/post_view/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,401)
        qs=Post.objects.filter(tag_name='python')
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Success:",response.status_code)
    
    def test_get_method_fail(self):
        url="http://127.0.0.1:8000/post_view/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,401)
        qs=Post.objects.filter(tag_name='python',post_name = "googal")
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Fail:",response.status_code)'''
    
'''class Post_update(APITestCase):
    def test_get_method(self):
        url="http://127.0.0.1:8000/post_view/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,401)
        qs=Post.objects.filter(tag_name='python')
        self.assertEqual(qs.count(),0)
        print("GET Method status code for Success:",_response.status_code)
    
    def test_put_method_success(self):
        url="http://127.0.0.1:8000/post_update/2/"
        tag_name = "python",
        blog = "python",
        post_header = "python devloper",
        post_content = "fullstace devloper",
        user = 1
        
        response = self.client.post(url,format='json')
        self.assertEqual(response.status_code,401)
        print("PUT Method status code for Success:",response.status_code)
    def test_put_method_fail(self):
        url="http://127.0.0.1:8000/post_update/2/"
        tag_name = "python",
        blog = "python",
        post_header = "python devloper",
        post_content = "fullstace devloper",
        user = 1
        if user:
               _response = self.client.post(url,format='json')
               self.assertEqual(_response.status_code,401)
               print("PUT Method status code for fail:",_response.status_code)
               self.assertEqual(_response.status_code,401,False)
               
class User_Social1(APITestCase):
    def setUP(self):
        Social.objects.all(linkedin = "",
        twitter = "",
        instagram = "",
        facebook = "",
        user = "")
    def test_post_method_success(self):
        url="http://127.0.0.1:8000/user_social/"
        data={
            'linkedin' : "googal",
            'twitter' : "python",
            'instagram' : "food",
            'facebook' : "python devloper",
            'user' : "1"
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("POST Method status code for Success:",response.status_code)

class User_Social1(APITestCase):
    def setUP(self):
        Social.objects.all(linkedin = "googal",
        twitter = "",
        instagram = "",
        facebook = "",
        user = "")
    def test_post_method_success(self):
        url="http://127.0.0.1:8000/user_social/"
        linkedin = "googal",
        twitter = "python"
        instagram = "food",
        facebook = "python devloper",
        user = "1"
        if user :
            response = self.client.post('user_social/')
            self.assertEqual(response.status_code,404)
            print("POST Method status code for success:",401)    
            return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)
          
    def test_put_method_Success(self):
        url="http://127.0.0.1:8000/user_social/"
        data={
            'linkedin' : "googal",
            'twitter' : "python",
            'instagram' : "food",
            'facebook' : "python devloper",
            'user' : "1"
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("PUT Method status code for Success:",response.status_code)

    def test_put_method_fail(self):
        url="http://127.0.0.1:8000/user_social/"
        data={
            'linkedin' : "googal",
            'twitter' : "python",
            'instagram' : "food",
            'facebook' : "python devloper",
            'user' : "1"
            }

        _response = self.client.post(url,format='json')
        self.assertEqual(_response.status_code,401)
        print("PUT Method status code for fail:",_response.status_code)
        self.assertEqual(_response.status_code,401,False)

               
class User_Social_view(APITestCase):
    def setUP(self):
        Social.objects.all(linkedin = "",
        twitter = "",
        instagram = "",
        facebook = "",
        user = "")   
    def test_get_method_succes(self):
        url="http://127.0.0.1:8000/user_social_view/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,401)
        qs=Social.objects.all()
        self.assertEqual(qs.count(),0,True)
        print("GET Method status code for Success:",_response.status_code)
    
    def test_get_method_fail(self):
        url=""
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)
        qs=Social.objects.all()
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Fail:",response.status_code)
    
class User_Social_Update(APITestCase):
    def test_get_method(self):
        url="http://127.0.0.1:8000/user_social_view/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,401)
        qs=Social.objects.all()
        self.assertEqual(qs.count(),0)
        print("GET Method status code for Success:",_response.status_code)
    
    def test_put_method_succes(self):
        url="http://127.0.0.1:8000/user_social_update/2/"
        data={
            'linkedin' : "googal",
            'twitter' : "python",
            'instagram' : "food",
            'facebook' : "python devloper",
            'user' : "1"
            }
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("PUT Method status code for Success:",response.status_code)
    def test_put_method_fail(self):
        url="http://127.0.0.1:8000/user_social_update/2/"
        data={
            'linkedin' : "googal",
            'twitter' : "python",
            'instagram' : "food",
            'facebook' : "python devloper",
            'user' : "1"
            }
        response = self.client.put(data,format='')
        self.assertEqual(response.status_code,404)
        print("PUT Method status code for Fail:",response.status_code)

class User_About1(APITestCase):
    def setUP(self):
        About.objects.all(description = "",
        location = "",
        email = "",
        workad_at = "",
        Studied_at= "",
        user = "")
    def test_post_method(self):
        url="http://127.0.0.1:8000/user_about/"
        data={
            'description' : "googal is most popular brouser",
            'location' : "plasiya indor",
            'email' : "lokeshkaushik2509@gmail.com",
            'workad_at' : "python devloper",
            'Studied_at':"btec student",
            'user' : "1"
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("POST Method status code for Success:",response.status_code)

class User_About(APITestCase):
    def setUP2(self):
        About.objects.all(description = "",
        location = "",
        email = "",
        workad_at = "",
        Studied_at= "",
        user = "")
    def test_post_method_success2(self):
        url="http://127.0.0.1:8000/user_about/"
        description = "this post is a popular post",
        location = "indor",
        email = "lokesh@gmail.com",
        workad_at = "",
        Studied_at= "",
        user = "1"
        if user :
            response = self.client.post('user_about/')
            self.assertEqual(response.status_code,404)
            print("POST Method status code for success:",401)    
            return self.assertEqual(401,status.HTTP_401_UNAUTHORIZED)
        
    def test_post_method_fail(self):
        url="http://127.0.0.1:8000/user_about/"
        data={
            'description' : "googal is most popular brouser",
            'location' : "plasiya indor",
            'email' : "lokeshkaushik2509@gmail.com",
            'workad_at' : "python devloper",
            'Studied_at':"btec student",
            'user' : "1"
            }

        _response = self.client.post(url,format='json')
        self.assertEqual(_response.status_code,401)
        print("POST Method status code for fail:",_response.status_code)
        self.assertEqual(_response.status_code,401,False)
    
class User_About_View(APITestCase):
    def setUP(self):
        About.objects.all(description = "",
        location = "",
        email = "",
        workad_at = "",
        Studied_at= "",
        user = "")  
    def test_get_method(self):
        url="http://127.0.0.1:8000/user_about_view/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,401)
        qs=About.objects.all()
        self.assertEqual(qs.count(),0)
        print("GET Method status code for Success:",_response.status_code)

    def test_get_method_fail(self):
        url=""
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)
        qs=Social.objects.all()
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Fail:",response.status_code)
    

class User_About_Update(APITestCase):
    def test_get_method(self):
        url="http://127.0.0.1:8000/user_about_view/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,401)
        qs=About.objects.all()
        self.assertEqual(qs.count(),0)
        print("GET Method status code for Success:",_response.status_code)
    
    def test_put_method(self):
        url="http://127.0.0.1:8000/user_about_update/"
        data={
            'description' : "",
            'location' : "",
            'email' : "",
            'workad_at' : "",
            'Studied_at' : "",
            'user' : "" 
            }
        response = self.client.put(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("PUT Method status code for Success:",response.status_code)

    def test_put_method_fail(self):
        url="http://127.0.0.1:8000/user_social_update/2/"
        data={
            'description' : "",
            'location' : "",
            'email' : "",
            'workad_at' : "",
            'Studied_at' : "",
            'user' : "" 
            }
        response = self.client.put(data,format='')
        self.assertEqual(response.status_code,404)
        print("PUT Method status code for Fail:",response.status_code)

class User_Profile_Pic1(APITestCase):
    def setUP(self):
        User_Profile_Pic1.objects.all(background_image = "",
        images = "",
        Post = "",
        user = "")
    def test_get_method_success(self):
        url="http://127.0.0.1:8000/user_profile_pic/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,401)
        qs=Profile_Pic.objects.all()
        self.assertEqual(qs.count(),0,True)
        print("GET Method status code for Success:",response.status_code)
    
    def test_get_method_fail(self):
        url="http://127.0.0.1:8000/user_profile_pic/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,401)
        qs=Profile_Pic.objects.all()
        self.assertEqual(qs.count(),False)
        print("GET Method status code for Fail:",response.status_code)
    
    def test_post_method(self):
        url="http://127.0.0.1:8000/user_profile_pic/"
        data={
            'background_image' : "",
            'images' : "",
            'Post' : "",
            'user' : "1",
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("POST Method status code for Success:",response.status_code)
    def test_post_method_fail(self):
        url="http://127.0.0.1:8000/user_profile_pic/"
        data={
            'background_image' : "",
            'images' : "",
            'Post' : "",
            'user' : "1",
            }

        _response = self.client.post(url)
        self.assertEqual(_response.status_code,401)
        print("POST Method status code for fail:",_response.status_code)
        self.assertEqual(_response.status_code,401,False)

class User_Profile_pic_Update(APITestCase):
    def setUP2(self):
       Profile_Pic.objects.all(background_image = "",
        images = "",
        Post = "",
        user = "")
    def test_get_method_success(self):
        url="http://127.0.0.1:8000/user_profile_pic/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,401)
        qs=Profile_Pic.objects.all()
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Success:",response.status_code)
    
    
    def test_put_method_success2(self):
        url="http://127.0.0.1:8000/user_profile_pic_update/2/"
        background_image = "",
        images = "",
        Post = "",
        user = "1"
        if user :
            response = self.client.post(url,format='json')
            self.assertEqual(response.status_code,401)
            print("PUT Method status code for Success:",response.status_code)
    def test_Put_method_fail(self):
        url="http://127.0.0.1:8000/user_profile_pic/2/"
        background_image = ""
        images = "",
        Post = "",
        user = "1"
        _response = self.client.post(url)
        self.assertEqual(_response.status_code,404)
        print("PUT Method status code for fail:",_response.status_code)
        self.assertEqual(_response.status_code,404,False)
    

class CommentsViewSet(APITestCase):
    def setUP(self):
        Comments.objects.all(text= "",
        datetime = "",
        Post = "",
        user = "")
    def test_get_method(self):
        url="http://127.0.0.1:8000/Comments/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,200)
        qs=Comments.objects.all()
        self.assertEqual(qs.count(),0)
        print("GET Method status code for Success:",_response.status_code)
    def test_get_method_fail(self):
        url=""
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)
        qs=Comments.objects.all()
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Fail:",response.status_code)
    
    def test_post_method_(self):
        url="http://127.0.0.1:8000/Comments/"
        data={
            'texts' : "comments is a every blog post in a comment ",
            'datetime' : "",
            'Post' : "1",
            'user' : "2"
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,400)
        print("POST Method status code for Success:",response.status_code)
    def test_post_method_fail(self):
        url="http://127.0.0.1:8000/Comments/"
        data={
            'texts' : "comments is a every blog post in a comment ",
            'datetime' : "",
            'Post' : "1",
            'user' : "2"
            }

        _response = self.client.post(url,format='json')
        self.assertEqual(_response.status_code,400)
        print("PUT Method status code for fail:",_response.status_code)
        self.assertEqual(_response.status_code,400,False)

def Comments_delete(APITestCase):
    def test_delete_method_success(self):
        url="http://127.0.0.1:8000/Comments_delete/1/"
        response=self.client.delete(id=id) 
        self.assertEqual(response.status_code,401)
        print("DELETE Method status code for Success:",response.status_code)

    def test_delete_method_fail(self):
        url="http://127.0.0.1:8000/Comments_delete/1/"
        response=self.client.delete(format='json')
        self.assertEqual(response.status_code,401)
        print("DELETE Method status code for fail:",response.status_code)
    

class ReplyViewSet(APITestCase):
    def setUP(self):
        Reply.objects.all(Comments= "",
        datetime = "",
        content = "",
        user = "")
    def test_get_method_success2(self):
        url="http://127.0.0.1:8000/reply/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,200)
        qs=Reply.objects.all()
        self.assertEqual(qs.count(),0,True)
        print("GET Method status code for Success:",_response.status_code)
    def test_get_method_fail(self):
        url=""
        response=self.client.get(url)
        self.assertEqual(response.status_code,404)
        qs=Reply.objects.all()
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Fail:",response.status_code)
    def test_post_method_success(self):
        url="http://127.0.0.1:8000/reply/"
        data={
            'Comments' : "comments is a every blog post in a comment ",
            'content' : "this is a blog replay",
            'datetime' : "",
            'user' : "2"
        }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,400)
        print("POST Method status code for Success:",response.status_code)
    def test_post_method_fail(self):
        url="http://127.0.0.1:8000/reply/"
        data={
            'Comments' : "comments is a every blog post in a comment ",
            'content' : "this is a blog replay",
            'datetime' : "",
            'user' : "2"
            }

        _response = self.client.post(url,data,format='')
        self.assertEqual(_response.status_code,400)
        print("PUT Method status code for fail:",_response.status_code)
        self.assertEqual(_response.status_code,400,False)

def test_reply_delete(APITestCase):
    def test_reply_delete_method_success(self):
        url="http://127.0.0.1:8000/reply_delete/1/"
        _response=self.client.delete(id=id)
        self.assertEqual(_response.status_code,204)
        print("DELETE Method status code for Success:",_response.status_code)

    def test_delete_method_fail(self):
        url="http://127.0.0.1:8000/reply_delete/1/"
        response=self.client.delete(pk=id)
        self.assertEqual(response.status_code,404)
        print("DELETE Method status code for fail:",response.status_code)


class BlogPost(APITestCase):
    def setUP(self):
        Blog.objects.all(blog_name = "googal",
        tag_name = "python",
        blog = "python",
        images = "",
        user = "")
    def test_post_method(self):
        url="http://127.0.0.1:8000/create_blog/"
        data={
            'blog_name' : "googal",
            'tag_name' : "python",
            'blog' : "food",
            'images' : "",
            'created_date' :"",
            'update_date'  : "",
            'user' : "",
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("POST Method status code for Success:",response.status_code)

class BlogPost(APITestCase):
    def test_post_method_success(self):
        url="http://127.0.0.1:8000/create_blog/"
        data={
            'blog_name' : "googal",
            'tag_name' : "python",
            'blog' : "food",
            'images' : "",
            'created_date' :"",
            'update_date'  : "",
            'user' : "",
            }

        _response = self.client.post(url)
        self.assertEqual(_response.status_code,401)
        print("POST Method status code for success:",_response.status_code)
        self.assertEqual(_response.status_code,401,True)
    def test_post_method_fail(self):
        url="http://127.0.0.1:8000/create_blog/"
    
        blog_name = "this post is a popular post",
        tag_name = "indor",
        blog = "lokesh@gmail.com",
        images = "",
        created_date = "",
        update_date = "",
        user = "1"
        
        if user :
            _response = self.client.post('create_blog/')
            self.assertEqual(_response.status_code,404,True)
            print("POST Method status code for fail:",_response.status_code)
    
class Blog_view(APITestCase):
    def test_get_method_success(self):
        url="http://127.0.0.1:8000/blog_view/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,401)
        qs=Blog.objects.filter(tag_name='python')
        self.assertEqual(qs.count(),0,True)
        print("GET Method status code for Success:",_response.status_code)
    
    def test_get_method_fail(self):
        url="http://127.0.0.1:8000/blog_view/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,401)
        qs=Post.objects.filter(tag_name='python',post_name = "googal")
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Fail:",response.status_code)
    

class Blog_update(APITestCase):
    def setUP(self):
        Blog.objects.all(blog_name = "googal",
        tag_name = "python",
        images = "",
        user = "")
    def test_get_method(self):
        url="http://127.0.0.1:8000/blog_update/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,404)
        qs=Blog.objects.all()
        self.assertEqual(qs.count(),0)
        print("GET Method status code for Success:",_response.status_code)
    def test_put_method(self):
        url="http://127.0.0.1:8000/post_update/2/"
        data={
            'blog_name' : "googal",
            'tag_name' : "python",
            'images' : "",
            'user' : "1"
            }
        response = self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,401)
        print("PUT Method status code for Success:",response.status_code)
    def test_put_method_fail(self):
        url="http://127.0.0.1:8000/post_update/2/"
        data={
            'blog_name' : "googal",
            'tag_name' : "python",
            'images' : "",
            'user' : "1"
            }
        response = self.client.put(data,format='')
        self.assertEqual(response.status_code,404)
        print("PUT Method status code for Fail:",response.status_code)


class test_Blog_delete(APITestCase):
    def test_delete_method_success(self):
        url="http://127.0.0.1:8000/blog_delete/1/"
        _response=self.client.delete(url,format='json')
        self.assertEqual(_response.status_code,401)
        print("DELETE Method status code for Success:",_response.status_code)
    def test_delete_method_fail(self):
        url="http://127.0.0.1:8000/blog_delete/1/"
        _response=self.client.delete(url)
        self.assertEqual(_response.status_code,401)
        print("DELETE Method status code for fail:",_response.status_code)

class CategoryListView(APITestCase):
    def test_get_method_success(self):
        url="http://127.0.0.1:8000/Category/"
        _response=self.client.get(url)
        self.assertEqual(_response.status_code,200)
        qs=Blog.objects.filter(tag_name='python')
        self.assertEqual(qs.count(),0,True)
        print("GET Method status code for Success:",_response.status_code)
    
    def test_get_method_fail(self):
        url="http://127.0.0.1:8000/Category/"
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        qs=Post.objects.filter(tag_name='googal')
        self.assertEqual(qs.count(),0,False)
        print("GET Method status code for Fail:",response.status_code)'''
      
