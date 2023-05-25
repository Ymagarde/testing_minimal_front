import pytest
import string
import random
from PIL import Image
import io
from unittest.mock import MagicMock, patch


def random_string(string_length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters)for i in range(string_length))


@pytest.fixture
def user_data():
    return {
        'username': random_string(),
        'email': random_string()+'@gmail.com',
        'password': random_string(),
        'first_name': random_string(),
        'last_name':  random_string(),
        'number': '+' + str(random.randint(1, 999))
        + str(random.randint(100000000, 999999999))
    }


@pytest.fixture
def mocked_ddb_table():
    with patch('boto3.resource') as mock_ddb_resource:
        mock_ddb_table = MagicMock()
        mock_ddb_resource.return_value.Table.return_value = mock_ddb_table
        yield mock_ddb_table


@pytest.fixture
def mocked_resource():
    with patch('boto3.resource') as mocked_resource:
        yield mocked_resource


def imagee():
    img = Image.new("RGB", (128, 128), (255, 0, 0))
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()
    return img_bytes


@pytest.fixture
def post_data(blog_data):
    return {
        'post_name': random_string(),
        'tag_name': random_string(),
        'post_header': random_string(),
        'post_content': random_string(),
        'blog': "",
        'user': 1
        }


@pytest.fixture
def test_create_blog():
    return {
       "tag_name": random_string(),
       'blog_name': random_string(),
       'user': random_string(),
    }


@pytest.fixture
def blog_data():
    return {
        "user": 1,
        "tag_name": random_string(),
        "blog_name": random_string()
    }


def generate_random_url(base_url):
    length = 8
    random_string = ''.join(random.choices(string.ascii_letters +
                                           string.digits, k=length))
    random_url = f"{base_url}/{random_string}"
    return random_url


@pytest.fixture
def user_Social_data():
    base_url = "https://www.example.com"
    return {
        "user": 1,
        "linkedin": generate_random_url(base_url),
        "twitter": generate_random_url(base_url),
        "instagram": generate_random_url(base_url),
        "facebook": generate_random_url(base_url)
    }


@pytest.fixture
def about_data(user_data):
    return {
        "user": 1,
        "description": random_string(),
        "location": random_string(),
        "email": random_string()+"@gmail.com",
        "workad_at": random_string(),
        "Studied_at": random_string()
    }


@pytest.fixture
def create_user_data():
    return {
       'username': 1,
       'email': random_string()+'@gmail.com',
       'password': random_string(),
       'first_name': random_string(),
       'last_name':  random_string(),
       'number': '+'+str(random.randint(1, 999))
       + str(random.randint(100000000, 999999999))
    }


@pytest.fixture
def test_create_Profile_Pic():
    return {
            # 'background_image': "jivbbj.png",
            # 'images': "kjlkv.jpg",
            'user': 1
        }


@pytest.fixture
def Comments():
    return {
        "text": random_string()
    }


@pytest.fixture
def random_data():
    return {
        "email": random_string()+"@gmail.com",
        "password": random_string(),
        "username": random_string()
        }


@pytest.fixture
def reply():
    return {
        # "parent": random_string(),
        "content": random_string()
    }


@pytest.fixture
def post_all():
    return {
        "user": {
            "user": {
                "background_image": "",
                "images": ""
            },
            "first_name": "lokesh",
            "last_name": "kaushik"
        },
        "post_name": "googal",
        "tag_name": "#python",
        "post_header": "python developer",
        "post_content": "Google's content and product policies",
        "images": "",
        "document": "",
        "liked_by": [
            {
                "first_name": "",
                "last_name": ""
            }
        ],
        "total_likes": 1,
        "comment": [
            {
                "cid": 1,
                "Post": 1,
                "user": {
                    "user": {
                        "user": 1,
                        "background_image": "",
                        "images": ""
                    },
                    "first_name": "yogesh",
                    "last_name": "magerde"
                },
                "text": "comment is basically gives an explanation",
                "reply": [
                    {
                        "rid": 1,
                        "user": {
                            "user": {
                                "user": 1,
                                "background_image": "",
                                "images": ""
                            },
                            "first_name": "lokesh",
                            "last_name": "kaushik"
                        },
                        "Comments": 1,
                        "parent": "",
                        "content": "AAAA",
                    }
                ]
            }
        ]
    }
