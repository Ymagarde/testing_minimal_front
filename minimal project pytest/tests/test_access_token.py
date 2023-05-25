from django.contrib.auth import authenticate
from unittest.mock import MagicMock
from unittest.mock import patch
from django.test import Client
from django.urls import reverse
from django.db.utils import IntegrityError
from rest_framework.test import APIClient
from moto import mock_dynamodb
import unittest.mock
import pytest
import json
import string
import random
from email_login import settings
from rest_framework.authtoken.models import Token
from accounts.models import CustomUser


social_dict = {}
post_data_dic = {}
blog_data_dic = {}
Comments_data_dic = {}
user_data_dic = {}
reply_dict = {}
token = {}
categories = []


def random_string(string_length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters)for i in range(string_length))


@mock_dynamodb
@pytest.mark.django_db()
def test_registration(client, user_data):
    mocked_ddb_resource = MagicMock()
    with unittest.mock.patch('boto3.resource',
                             return_value=mocked_ddb_resource):
        mocked_ddb_table = MagicMock()
        mocked_ddb_resource.Table.return_value = mocked_ddb_table
        response = client.post(reverse('Register'),
                               json.dumps(user_data),
                               content_type='application/json')
        assert response.status_code == 201


@patch('boto3.resource')
@pytest.mark.django_db()
def test_login(mocked_resource, client, user_data, id=None):
    mocked_table = MagicMock()
    test_registration(client, user_data)
    mocked_table.query.return_value = {
        'Items': [{'username': user_data['email'],
                   'password': user_data['password']}]}
    response = client.post(reverse('login'), user_data,
                           content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_forgot_password(client, user_data):
    user = CustomUser.objects.create_user(**user_data)
    with unittest.mock.patch(
         'django.contrib.auth.authenticate') as mock_authenticate:
        mock_authenticate.return_value = authenticate
    response = client.post(reverse('forget_password'),
                           {'email': user_data['email']},
                           content_type='application/json')
    assert response.status_code == 202
    send_password_reset_email = MagicMock(return_value=True)
    send_password_reset_email(to=[user_data['email']],
                              subject='Password reset request',
                              message='Reset your password',
                              email_from=settings.EMAIL_HOST_USER)
    send_password_reset_email.assert_called_once()
    user = CustomUser.objects.get(
        email=user_data['email'])
    assert user.forget_password_token is not None
    if response.status_code != 202:
        print({"message": "Unauthorized User"})
    assert response.status_code == 202


@pytest.mark.django_db
def test_change_password(client, user_data):
    change_password_data = {
        'new_password': random_string(),
        'confirm_password': random_string()}
    with unittest.mock.patch(
        'django.contrib.auth.authenticate'
    ) as mock_authenticate:
        mock_authenticate.return_value = authenticate(
            test_forgot_password(client, user_data)
            )
    user = CustomUser.objects.create_user(username='testuser')
    user.forget_password_token = 'token'
    user.save()
    with unittest.mock.patch(
        'django.contrib.auth.authenticate'
    ) as mock_authenticate:
        mock_authenticate.return_value = authenticate
    response = client.post(reverse(
        'change_password', kwargs={'token': 'token'}),
                        change_password_data, content_type='application/json')
    if response.status_code != 205:
        print({'message': "Invalid credentials, try again"})
    assert response.status_code == 205
    assert response.data['message'] == 'Password change successfully now login'
    user = CustomUser.objects.get(username='testuser')
    assert user.check_password(change_password_data['new_password']) is True


@patch('boto3.resource')
@pytest.mark.django_db
def test_blog_data(client, blog_data, create_user_data, id=None):
    user = CustomUser.objects.create_user(create_user_data)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("blog")
    response = client.post(url, blog_data)
    response_data = response.json()
    for key, value in blog_data.items():
        assert key in response_data
        assert response_data[key] == value
        blog_data_dic[key] = value
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_get_blog_data(mocked_resource, client,
                       create_user_data, blog_data):
    user = CustomUser.objects.create_user(create_user_data)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post(reverse('blog'), blog_data)
    assert response.status_code == 200
    url = "http://127.0.0.1:8000/blog_view/"
    response = client.get(url)
    print(response.content)
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db()
def test_blog_update(mocked_resource, client,
                     create_user_data, blog_data, random_data):
    test_blog_data(client, blog_data, create_user_data)
    user = CustomUser.objects.create_user(
        email=random_data["email"],
        password=random_data["password"],
        username=random_data["username"])
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(reverse('blog_update', args='1'), blog_data)
    assert response.status_code == 205


@patch('boto3.resource')
@pytest.mark.django_db()
def test_blog_delete(mocked_resource, client,
                     create_user_data, blog_data, random_data):
    test_blog_data(client, blog_data, create_user_data)
    try:
        user = CustomUser.objects.create_user(
            email=random_data["email"],
            password=random_data["password"],
            username=random_data["username"])
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed to create user with email address")
    print(blog_data_dic)
    response = client.get(reverse('blog_delete', args="1"))
    assert response.data == {'message': 'Your blog delete successfully'}
    assert response.status_code == 205


@patch('boto3.resource')
@pytest.mark.django_db
def test_post_data(mocked_resource, client, post_data,
                   create_user_data, blog_data,
                   random_data, id=None):
    test_blog_data(client, blog_data, create_user_data)
    post_data["blog"] = blog_data_dic["user"]
    try:
        user = CustomUser.objects.create_user(
            email=random_data["email"],
            username=random_data["username"],
            password=random_data["password"])
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed to create user with email address")
    url = reverse("user_post")
    response = client.post(url, post_data)
    blog_data_dic["blog_id"] = response.json()["id"]
    response_data = response.json()
    for key, value in post_data.items():
        assert key in response_data
        assert response_data[key] == value
        post_data_dic[key] = value
        print(f"{key}: {response_data[key]}")
    post_data_dic["post_id"] = response.json()["id"]
    assert response.status_code == 201


@patch('boto3.resource')
@pytest.mark.django_db
def test_get_post_data(mocked_resource, client, post_data, create_user_data,
                       blog_data, post_all, random_data):
    test_blog_data(client, blog_data, create_user_data)
    user = CustomUser.objects.create_user(
        email=random_data["email"],
        username=random_data["username"],
        password=random_data["password"])
    post_data["blog"] = blog_data_dic["user"]
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("user_post")
    response = client.post(url, post_data)
    print(response.content)
    assert response.status_code == 201
    url = "http://127.0.0.1:8000/user_post_data/1/"
    response = client.get(url)
    print(response.content)
    response_data = response.json()
    post_all['data'] = response_data
    print(post_all)
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_post_view(mocked_resource, client, post_data,
                   blog_data, create_user_data, random_data):
    test_blog_data(client, blog_data, create_user_data)
    user = CustomUser.objects.create_user(
        email=random_data["email"],
        username=random_data["username"],
        password=random_data["password"])
    post_data["blog"] = blog_data_dic["user"]
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("user_post")
    response = client.post(url, post_data)
    assert response.status_code == 201
    url = reverse("view_post")
    response = client.get(url)
    print(response.json())
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_Post_update(mocked_resource, client,
                     create_user_data, post_data,
                     blog_data, random_data, id=None):
    test_post_data(mocked_resource, client, post_data,
                   create_user_data, blog_data, random_data)
    user = CustomUser.objects.create_user(
        email=random_string()+"@gmail.com",
        password=random_string(),
        username=random_string())
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.put(reverse('post_update', args='1'), post_data)
    print(response.content)
    assert response.status_code == 205


@patch('boto3.resource')
@pytest.mark.django_db
def test_about_user(client, about_data, create_user_data, id=None):
    user = CustomUser.objects.create_user(create_user_data)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("User_About")
    response = client.post(url, about_data)
    print(response.status_code)
    response_data = response.json()
    for key, value in about_data.items():
        assert key in response_data
        assert response_data[key] == value
        user_data_dic[key] = value
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_get_about_user(client, about_data, create_user_data):
    user = CustomUser.objects.create_user(create_user_data)
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post(reverse('User_About'), about_data)
    assert response.status_code == 200
    url = "http://127.0.0.1:8000/about/1/"
    response = client.get(url)
    response_data = response.json()
    for key, value in about_data.items():
        assert key in response_data
        assert response_data[key] == value
        print(f"{key}: {response_data[key]}")
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_get_about_user_view(client, about_data, random_data):
    user = CustomUser.objects.create_user(
        email=random_data["email"],
        username=random_data["username"],
        password=random_data["password"])
    client = APIClient()
    client.force_authenticate(user=user)
    response = client.post(reverse('User_About'), about_data)
    assert response.status_code == 200
    url = "http://127.0.0.1:8000/user_about_view/"
    response = client.get(url)
    response_data = response.json()[0]
    for key, value in about_data.items():
        assert key in response_data
        assert response_data[key] == value
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_about_update(client, random_data, about_data):
    user = CustomUser.objects.create_user(
        email=random_data["email"],
        username=random_data["username"],
        password=random_data["password"])
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("User_About")
    response = client.post(url, about_data)
    assert response.status_code == 200
    response = client.put(reverse('User_About_Update'), about_data)
    print(response.content)
    assert response.status_code == 205


@patch('boto3.resource')
@pytest.mark.django_db
def test_social(client, user_Social_data, create_user_data, id=None):
    user = CustomUser.objects.create_user(create_user_data)
    token = Token.objects.create(user=user)
    client = APIClient()
    client.force_authenticate(user=user)
    url = ("http://127.0.0.1:8000/user_social/")
    response = client.post(url, user_Social_data)
    response_data = response.json()
    social_dict["token"] = token
    for key, value in user_Social_data.items():
        assert key in response_data
        assert response_data[key] == value
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_get_social(client, user_Social_data, create_user_data):
    user = CustomUser.objects.create_user(create_user_data)
    client = APIClient()
    client.force_authenticate(user=user)
    url = ("http://127.0.0.1:8000/user_social/")
    response = client.post(url, user_Social_data)
    assert response.status_code == 200
    url = "http://127.0.0.1:8000/user_social/"
    response = client.get(url)
    response_data = response.json()[0]
    for key, value in user_Social_data.items():
        assert key in response_data
        assert response_data[key] == value
        print(f"{key}: {response_data[key]}")
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_get_social_user_view(client, user_Social_data, random_data):
    user = CustomUser.objects.create_user(
        email=random_data["email"],
        username=random_data["username"],
        password=random_data["password"])
    client = APIClient()
    client.force_authenticate(user=user)
    url = ("http://127.0.0.1:8000/user_social/")
    response = client.post(url, user_Social_data)
    assert response.status_code == 200
    url = "http://127.0.0.1:8000/user_social_view/"
    response = client.get(url)
    print(response.content)
    response_data = response.json()[0]
    for key, value in user_Social_data.items():
        assert key in response_data
        assert response_data[key] == value
        print(f"{key}: {response_data[key]}")
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_social_update(client, random_data, user_Social_data):
    user = CustomUser.objects.create_user(
        email=random_data["email"],
        username=random_data["username"],
        password=random_data["password"])
    client = APIClient()
    client.force_authenticate(user=user)
    url = ("http://127.0.0.1:8000/user_social/")
    response = client.post(url, user_Social_data)
    assert response.status_code == 200
    response = client.put(reverse('User_Social_Update'), user_Social_data)
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_comment_data(mocked_resource, client, post_data,
                      create_user_data,
                      blog_data, Comments,
                      random_data, id=None):
    test_post_data(mocked_resource, client, post_data,
                   create_user_data, blog_data,
                   random_data)
    Comments["Post"] = post_data_dic["post_id"]
    Comments["user"] = post_data_dic["user"]
    Comments["text"] = "dhkajsch"
    try:
        user = CustomUser.objects.create_user(
                    username=random_string(),
                    password=random_string(),
                    email=random_string()+"@gmail.com")
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed to create user with email address")
    response = client.post("/Comments/", Comments)
    response_data = response.json()
    Comments_data_dic["user"] = response.json()["user"]
    Comments_data_dic["cid"] = response.json()["cid"]
    for key, value in Comments.items():
        assert key in response_data
        assert response_data[key] == value
        print(f"{key}: {response_data[key]}")
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_Comments_delete(mocked_resource,
                         client, post_data, create_user_data,
                         blog_data, Comments, random_data):
    test_comment_data(mocked_resource, client, post_data,
                      create_user_data, blog_data,
                      Comments, random_data)
    client = Client()
    try:
        user = CustomUser.objects.create_user(
                    email=random_string()+"@gmail.com",
                    password=random_string(),
                    username=random_string())
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed to create user with email address")
    response = client.delete(reverse('Comments_delete', args='1'))
    assert response.status_code == 200
    assert response.data == "Comments is successfully delete"


@patch('boto3.resource')
@pytest.mark.django_db
def test_Profile_Pic(client, test_create_Profile_Pic,
                     create_user_data, id=None):
    user = CustomUser.objects.create_user(create_user_data)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("user_profile_pic")
    response = client.post(url, test_create_Profile_Pic)
    print({"response": response.content})
    print(response.status_code)
    response_data = response.json()
    for key, value in test_create_Profile_Pic.items():
        assert key in response_data
        assert response_data[key] == value
        print(f"{key}: {response_data[key]}")
    assert response.status_code == 201


@patch('boto3.resource')
@pytest.mark.django_db
def test_get_profile_pic(client, test_create_Profile_Pic,
                         create_user_data):
    user = CustomUser.objects.create_user(create_user_data)
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("user_profile_pic")
    response = client.post(url, test_create_Profile_Pic)
    assert response.status_code == 201
    url = "http://127.0.0.1:8000/profilepik/1/"
    response = client.get(url)
    response_data = response.json()
    print(response_data)
    for key, value in test_create_Profile_Pic.items():
        assert key in response_data
        assert response_data[key] == value
        print(f"{key}: {response_data[key]}")
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_profile_pic_update(client, random_data, test_create_Profile_Pic):
    user = CustomUser.objects.create_user(
                email=random_data["email"],
                username=random_data["username"],
                password=random_data["password"])
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("user_profile_pic")
    response = client.post(url, test_create_Profile_Pic)
    assert response.status_code == 201
    response = client.put(reverse('User_Profile_Pic_Update'),
                          test_create_Profile_Pic)
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_like_data(mocked_resource, client, post_data,
                   create_user_data, blog_data, random_data):
    test_post_data(mocked_resource, client, post_data, create_user_data,
                   blog_data, random_data)
    try:
        user = CustomUser.objects.create_user(
                    email=random_string()+"@gmail.com",
                    password=random_string(),
                    username=random_string())
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed to create user with email address")
    no_of_post = post_data_dic["post_id"]
    url = reverse("like_post", args=[no_of_post])
    response = client.post(url,)
    assert response.status_code == 202


@patch('boto3.resource')
@pytest.mark.django_db
def test_reply_data(mocked_resource, user_data,
                    client, post_data, create_user_data,
                    blog_data, Comments, random_data, reply, id=None):
    test_comment_data(mocked_resource, client, post_data, create_user_data,
                      blog_data, Comments, random_data)
    reply["Comments"] = Comments_data_dic["cid"]
    reply["user"] = Comments_data_dic["user"]
    try:
        user = CustomUser.objects.create_user(
                    email=random_string()+"@gmail.com",
                    password=random_string(),
                    username=random_string())
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed to create user with email address")
    response = client.post("/reply/", reply)
    response_data = response.json()
    print(response_data['rid'])
    reply_dict['id'] = response_data['rid']
    for key, value in reply.items():
        assert key in response_data
        assert response_data[key] == value
        print(f"{key}: {response_data[key]}")
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_reply_delete(mocked_resource, client, post_data, create_user_data,
                      blog_data, reply, random_data, user_data, Comments):
    test_reply_data(mocked_resource, user_data,
                    client, post_data, create_user_data,
                    blog_data, Comments, random_data, reply)
    client = Client()
    try:
        user = CustomUser.objects.create_user(
                    email=random_string()+"@gmail.com",
                    password=random_string(),
                    username=random_string())
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed to create user with email address")
    response = client.delete(reverse('reply_delete', args='1'))
    assert response.status_code == 200
    assert response.data == "Reply  is successfully delete"


@patch('boto3.resource')
@pytest.mark.django_db
def test_category_list(
            random_data, client, mocked_resource, blog_data, create_user_data):
    test_blog_data(client, blog_data, create_user_data)
    client = Client()
    try:
        print(type(random_data["password"]))
        user = CustomUser.objects.create_user(
                    email=random_string()+"@gmail.com",
                    password=random_string(),
                    username=random_string())
        client = APIClient()
        client.force_authenticate(user=user)
    except IntegrityError:
        print("Failed")
    mocked_resource.patch(
                "blog.models.Blog.objects.all",
                return_value=[blog_data])
    url = "http://127.0.0.1:8000/Category/"
    response = client.get(url)
    response_data = response.json()
    print(response_data)
    for key, value in blog_data.items():
        assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_post_view_user(
            client, blog_data, random_data, create_user_data,
            post_data, post_all):
    test_blog_data(client, blog_data, create_user_data)
    user = CustomUser.objects.create_user(
            email=random_data["email"],
            username=random_data["username"],
            password=random_data["password"])
    post_data["blog"] = blog_data_dic["user"]
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("user_post")
    response = client.post(url, post_data)
    print(response.content)
    assert response.status_code == 201
    url = "http://127.0.0.1:8000/post_view_user/"
    response = client.get(url, post_data, format="json")
    response_data = response.json()
    post_all['data'] = response_data
    print(post_all)
    assert response.status_code == 200


@patch('boto3.resource')
@pytest.mark.django_db
def test_post_view_all(
            client, blog_data, create_user_data, post_data,
            post_all, random_data):
    test_blog_data(client, blog_data, create_user_data)
    user = CustomUser.objects.create_user(
            email=random_data["email"],
            username=random_data["username"], password=random_data["password"])
    post_data["blog"] = blog_data_dic["user"]
    client = APIClient()
    client.force_authenticate(user=user)
    url = reverse("user_post")
    response = client.post(url, post_data)
    assert response.status_code == 201
    url = "http://127.0.0.1:8000/post_view/"
    response = client.get(url)
    response_data = response.json()
    post_all['data'] = response_data
    print(post_all)
    for key, value in post_all.items():
        assert response.status_code == 200
