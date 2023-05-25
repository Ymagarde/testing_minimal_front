
from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from mptt.forms import TreeNodeChoiceField

class customuser_serializer(serializers.ModelSerializer):
    class Meta:
        model= CustomUser
        fields = ['email','number','forget_password_token']

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email','username','password','first_name','last_name','number')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class Profile_Pic_serializer123(serializers.ModelSerializer):
    class Meta:
        model = Profile_Pic
        fields =['user','background_image','images']
 

class RegisterSerializer12(serializers.ModelSerializer):
    user = Profile_Pic_serializer123(many=False,read_only=True,required=False)
    
    class Meta:
        model = CustomUser
        fields = ('user','first_name','last_name')

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)



class LoginSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'password')

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')        

class forget_password_serializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email',) 

class Reset_password_serializer(serializers.ModelSerializer):
    class Meta:
        model = change_password
        fields =('new_password','confirm_password')

class Social_serializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields ='__all__'


class About_serializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields ='__all__'

class Profile_Pic_serializer(serializers.ModelSerializer):
    class Meta:
        model = Profile_Pic
        fields =['id','user','background_image','images']
    
class Profile_Pic_serializerField12(serializers.ModelSerializer):
    class Meta:
        model = Profile_Pic
        fields =['user','images','background_image']


class ReplySerializer(serializers.ModelSerializer):
    
    parent = TreeNodeChoiceField(queryset = Reply.objects.all())
    def __init__(self, instance=None, data=..., **kwargs):
            super().__init__(instance, data, **kwargs)
        
            self.fields['parent'].lablel = ''
            self.fields['parent'].required = False
    class Meta:
        model = Reply
        fields = ['rid','user','Comments','parent','content','datetime']

class ReplySerializer1(serializers.ModelSerializer):
    
    parent = TreeNodeChoiceField(queryset = Reply.objects.all())
    
    def __init__(self, instance=None, data=..., **kwargs):
            super().__init__(instance, data, **kwargs)
        
            self.fields['parent'].lablel = ''
            self.fields['parent'].required = False
    user = RegisterSerializer12(many=False,read_only=True)
    class Meta:
        model = Reply
        fields = ['rid','user','Comments','parent','content','datetime']
    


class CommentsSerializer(serializers.ModelSerializer):
    user = RegisterSerializer12(many=False,read_only=True)
    reply = ReplySerializer1(many=True,read_only=True)
    
    class Meta:
        model = Comments
        fields =['cid','Post','user','datetime','text','reply']

class CommentsSerializer1(serializers.ModelSerializer):
    
    class Meta:
        model = Comments
        fields =['cid','Post','user','datetime','text']
       
    


class User_Post_serializer(serializers.ModelSerializer):
    comment = CommentsSerializer(many=True, read_only=True)
    liked_by = RegisterSerializer12(many=True,read_only=True)
    total_likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','user','post_name','tag_name','blog','post_header','post_content','images','document','liked_by','total_likes','created_date','update_date','is_active','comment']
    def get_total_likes(self, instance):
          return instance.liked_by.count()

class User_Post_get_serializer(serializers.ModelSerializer):
    user = RegisterSerializer12(many=False,read_only=True)
    comment = CommentsSerializer(many=True, read_only=True)
    liked_by = RegisterSerializer12(many=True,read_only=True)
    total_likes = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id','user','post_name','tag_name','blog','post_header','post_content','images','document','liked_by','total_likes','created_date','update_date','is_active','comment']
    def get_total_likes(self, instance):
          return instance.liked_by.count()
 
class BlogSerializer(serializers.ModelSerializer):
    group_set = Profile_Pic_serializer(many=True, read_only =True)
    class Meta:
        model = Blog
        fields = ['id','tag_name','blog_name','created_date','update_date','user','images','group_set']
        
    def create(self, validated_data):
        return Blog.objects.create(**validated_data)


class Videoserializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields ='__all__'


