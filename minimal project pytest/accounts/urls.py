
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from accounts.views import *
from . import views
urlpatterns = [
    
    path('login/', Login.as_view(), name="login"),
    path('register/', Register.as_view(), name="Register"),
    path('forget_password/',Forget_password.as_view(), name="forget_password"),
    path('change-password/<token>/',ChangePassword.as_view(), name="change_password"),
    path('user_post/',User_Post.as_view(),name='user_post'),
    path('post_view_user/',Post_view_user.as_view(),name='Post_view_user'),
    path('post_view/',Post_view.as_view(),name='view_post'),
    path('post_update/<int:pk>/',Post_update.as_view(),name='post_update'),
    path('user_social/', User_Social.as_view(),name='user_social'),
    path('user_social_view/',User_Social_view.as_view(),name='user_social'),
    path('user_social_update/',User_Social_Update.as_view(),name='User_Social_Update'),
    path('user_about/', User_About.as_view(),name='User_About'),
    path('user_about_view/',User_About_View.as_view(),name='View_User_About'),
    path('user_about_update/', User_About_Update.as_view(),name='User_About_Update'),
    path('user_profile_pic/', User_Profile_Pic.as_view(),name='user_profile_pic'),
    path('user_profile_pic_update/',User_Profile_pic_Update.as_view(),name='User_Profile_Pic_Update'),
    path('like/<int:id>',views.Like_Post,name='like_post'),
    path('Comments/', CommentsViewSet.as_view()),
    path('Comments_delete/<int:pk>/',views.Comments_delete, name='Comments_delete'),
    path('reply/', ReplyViewSet.as_view()),
    path('reply_delete/<int:pk>/',views.reply_delete, name='reply_delete'),
    path('postdetail/<int:pk>/',PostDetail.as_view(),name='PostDetail'),
    path('create_blog/',BlogPost.as_view(),name='blog'),
    path('blog_view/',Blog_view.as_view(),name='blog_view'),
    path('blog_update/<int:pk>/',Blog_update.as_view(),name='blog_update'),
    path('blog_delete/<int:pk>/',Blog_delete.as_view(),name='blog_delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('show/',views.show,name='show'),
    path('video/<int:pk>/',views.video,name='video'),
    path('view_all_posts/',views.View_all_Posts,name='post'),
    path('Category/',CategoryListView.as_view()),
    path('user_post_data/<int:pk>/',Post_data.as_view()),
    path('profilepik/<int:pk>/',Profile_data.as_view()),
    path('about/<int:pk>/',About_data.as_view()),
    path('sociale/<int:pk>/',social_data.as_view()),
   
]