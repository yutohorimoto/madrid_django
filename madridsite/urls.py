from django.urls import path

from . import views

urlpatterns = [
    path('',views.home_page, name='home'),
    path('result',views.result_page, name='result'),
    path('member',views.member_page, name='member'),
    path('quiz',views.quiz_page, name='quiz'),
    path('poll',views.poll_page, name='poll'),
    path('diagnosis',views.diagnosis, name='diagnosis'),
    path('diagnosis_result',views.diagnosis_result, name='diagnosis_result'),
    path('news', views.NewsListView.as_view(), name='news_list'),
    path('like/<int:id>', views.like, name='like'),
    path(r'create/', views.create_account, name='create_account'),
    path(r'login/', views.account_login, name='login'),
    path("logout/",views.MyLogoutView.as_view(template_name='madridsite/logout.html'),name="logout"),
    path('accounts/login/',views.account_login, name='account_login'),
]
    #path('home',views.home_page, name='home'),
