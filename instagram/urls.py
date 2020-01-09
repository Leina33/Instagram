from django.conf.urls import url
from . import views




urlpatterns = [

    
    url('', views.index,name = 'insta-home'),
    url('post/update/<int:pk>',views.PostUpdateView.as_view(), name ='post-update'),

    url('post/<int:pk>/',views.PostDetailView.as_view(), name ='post-detail'),
    url('post/<int:pk>/update',views.PostUpdateView.as_view(), name ='post-update'),

    url('post/comment/<int:pk>/',views.comment, name ='post-comment'),


    url('post/new/', views.CreatePost.as_view(), name='create-post'),

    url (r'^search/',views.search_results,name= 'search_results'),
    url('like/<int:id>',views.upvote,name='like'),
    url('dislike/<int:id>',views.downvote,name='dislike'),
    url('home/<username>/',views.user_detail, name = 'user_follow'),



]
