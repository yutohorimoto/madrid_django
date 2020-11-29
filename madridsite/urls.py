from django.urls import path
from django.contrib.auth import login, logout
from . import views
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home_page, name='home'),
    path('result',views.result_page, name='result'),
    path('member',views.member_page, name='member'),
    path('quiz',views.quiz_page, name='quiz'),
    path('poll',views.poll_page, name='poll'),
    path('poll_result',views.poll_result, name='poll_result'),
    path('post', views.PostListView.as_view(), name='post_list'),
    #path('post/new/', views.post_new, name='post_new'),
    path('post/new/', views.NewPost.as_view(), name='post_new'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('diagnosis',views.diagnosis, name='diagnosis'),
    path('diagnosis_result',views.diagnosis_result, name='diagnosis_result'),
    path('news', views.NewsListView.as_view(), name='news_list'),
    #path('news', views.news_list, name='news_list'),
    path('like/<int:id>', views.like, name='like'),
    path(r'create/', views.create_account, name='create_account'),
    path(r'login/', views.account_login, name='login'),
    path("logout/",views.MyLogoutView.as_view(template_name='madridsite/logout.html'),name="logout"),
    path('accounts/login/',views.account_login, name='account_login'),
    path('news/mylike',views.MyLikeView.as_view(),name ='mylike'),
     url(r'mdeditor/', include('mdeditor.urls')) # 追加

]
    #path('home',views.home_page, name='home'),
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

