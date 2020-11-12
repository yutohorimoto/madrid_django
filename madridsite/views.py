from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.views import View
from django.views.generic import CreateView, TemplateView,ListView,DetailView,DeleteView,FormView
from django.utils import timezone
from .models import Post,News,Like
from .forms import UserCreateForm, LoginForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect 
from django.utils.functional import cached_property


def home_page(request):
    return render(request, 'madridsite/home.html')

def result_page(request):
    return render(request, 'madridsite/result.html')

def member_page(request):
    return render(request, 'madridsite/member.html')

def quiz_page(request):
    return render(request, 'madridsite/quiz.html')

def poll_page(request):

    return render(request, 'madridsite/poll.html')

class NewsListView(ListView):
    template_name = 'madridsite/news.html'
    #model = News
    queryset = News.objects.order_by('id').reverse()
    context_object_name = 'realnews'
    paginate_by = 20
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['check'] = Like.objects.filter(user=self.request.user, news=self.kwargs.get('id')).exists()
        
        return context


def diagnosis(request):

    return render(request, 'madridsite/diagnosis.html')
def diagnosis_result(request):
#def diagnosis_result(self, request, *args, **kwargs):

    q1 = int(request.POST['q1'])
    q2 = int(request.POST['q2'])
    q3 = int(request.POST['q3'])
    q4 = int(request.POST['q4'])
    q5 = int(request.POST['q5'])
    result=''
    fav=[result,q1,q2,q3,q4,q5]
  
    madrid=['レアルマドリード',2,2,3,5,1]

    barcerona=['バルセロナ',4,5,5,5,2]

    atletico=['アトレティコマドリード',1,1,2,3,5]
   
    juventus=['ユベントス',3,4,3,4,2]
    
    milan=['ミラン',2,3,1,3,2]
    
    intel=['インテル',3,1,2,4,4]
    
    bayern=['バイエルン',5,4,3,5,5]
    
    paris=['パリサンジェルマン',5,5,5,5,3]
    
    city=['マンチェスターシティ',5,5,5,4,5]
    
    united=['マンチェスターユナイテッド',2,1,1,5,2]
   
    arsenal=['アーセナル',2,3,4,3,1]
    
    chelsea=['チェルシー',4,4,3,4,2]
    
    liverpool=['リヴァプール',4,2,3,4,4]
    
    sevilia=['セビージャ',1,3,4,2,4]

    spurs=['トッテナム',2,1,1,3,4]

    bvb=['ドルトムント',5,2,4,4,3]

    leipzig=['ライプツィヒ',4,5,2,1,5]

    atalanta=['アタランタ',5,5,4,1,4]

    napoli=['ナポリ',3,4,4,2,3]

    lazio=['ラツィオ',3,2,2,1,4]

    rome=['ローマ',4,3,2,3,3]

    marseille=['マルセイユ',2,4,3,1,2]

    lyon=['リヨン',1,2,2,2,2]

    borussia=['ボルシアMG',3,3,3,2,3]

    
    teams=[madrid,barcerona,atletico,juventus,bayern,paris,city,united,arsenal,chelsea,liverpool,milan,intel,
    sevilia,spurs,bvb,leipzig,atalanta,napoli,lazio,rome,marseille,lyon,borussia]

    distance=1000
    
    for i in range(24):
        dis = 0
        for n in range(5):
            dis += pow(teams[i][n+1]-fav[n+1],2)
        
        if dis<distance:
            distance = dis
            result = teams[i][0]

    context = {
        'result': result,
    }
    return render(request, 'madridsite/diagnosis_result.html', context)
    


#アカウント作成
class Create_account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, 'madridsite/create.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'madridsite/create.html', {'form': form,})

create_account = Create_account.as_view()

#ログイン機能
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = User.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'madridsite/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'madridsite/login.html', {'form': form,})

account_login = Account_login.as_view()


#def Account_logout(request):

#    logout(request,user)
#    return render(request, 'mybook/logout.html')

class MyLogoutView(auth_views.LogoutView):
    
    # ログアウト時に表示されるテンプレート
    template_name = "templates/madridsite/logout.html"

@login_required
def like(request,id):
#def like(request, *args, **kwargs):
    news = get_object_or_404(News, id=id)
    
    is_like = Like.objects.filter(user=request.user).filter(news=news).count()
    
    if is_like > 0:
        #liking = Like.objects.get(user=request.user,post__id=kwargs['post_id'])
        liking = Like.objects.get(user=request.user,news=news)
        liking.delete()
        news.like_number -= 1
        news.save()
        
        return redirect('news_list')
        
    news.like_number += 1
    news.save()
    like = Like()
    like.user = request.user
    like.news = news
    like.save()
    
    return redirect('news_list')