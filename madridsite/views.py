from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.views import View
from django.views.generic import CreateView, TemplateView,ListView,DetailView,DeleteView,FormView
from django.utils import timezone
from .models import Post,News,Like,Election,Comment
from .forms import UserCreateForm, LoginForm,PostForm,CommentForm
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
    #polls =  get_object_or_404(Poll)
    polls = Election.objects.all()
    return render(request, 'madridsite/poll.html', {'polls':polls})

def poll_result(request):
    polls = Election.objects.all()
    
    if request.method == 'POST':
        vote = request.POST['cn']
        poll =  get_object_or_404(Election,id=vote)
        poll.number += 1
        poll.save()

    return render(request, 'madridsite/poll_result.html', {'polls':polls})

class PostListView(ListView):
    template_name = 'madridsite/post_list.html'
    #model = Post
    queryset = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context_object_name = 'posts'

class PostDetail(DetailView):
    template_name = 'madridsite/post_detail.html'
    model = Post
    context_object_name = 'post'
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
    #    context['check'] = Like.objects.filter(user=self.request.user, post=self.kwargs.get('pk')).exists()
        context['comments']= Comment.objects.filter(post=self.kwargs.get('pk'))
        return context

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            #commit=False は Post モデルをまだ保存しないという意味
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
            #新しく作成されたポストの post_detail ページに移動
    else:
        form = PostForm()
    return render(request, 'madridsite/post_edit.html', {'form': form})

class NewPost(LoginRequiredMixin,CreateView,):
    model = Post
    form_class = PostForm
    template_name = "madridsite/post_edit.html"
    success_url = "post_list"  

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #編集したいPost モデルを取得
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        #formを保存するとき
        if form.is_valid():
            post = form.save(commit=False)
            if post.author == request.user:
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
            else:
                raise PermissionDenied

    else:
        form = PostForm(instance=post)
        #formを開くだけのとき
    return render(request, 'madridsite/post_edit.html', {'form': form})

class PostDelete(DeleteView):
    template_name = 'madridsite/post_confirm_delete.html'
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('post_list')

def news_list(request):
    news = News.objects.order_by('id').reverse()
    if request.method == 'POST':
        from django.http import QueryDict
        # request.bodyに入っている。
        dic = QueryDict(request.body, encoding='utf-8')
        view_number = int(dic.get('view_number'))
        news_number = int(dic.get('news_number'))
        
        viewed_news = get_object_or_404(News, id=news_number)
        viewed_news.view_number += view_number
        viewed_news.save()

    return render(request, 'madridsite/news.html', {'realnews':news})

class NewsListView(ListView):
    template_name = 'madridsite/news.html'
    #model = News
    queryset = News.objects.order_by('id').reverse()
    context_object_name = 'realnews'
    paginate_by = 20
    def post(self, request, *args, **kwargs):
        #if self.request.method == 'POST':
        from django.http import QueryDict
        # request.bodyに入っている。
        dic = QueryDict(self.request.body, encoding='utf-8')
        view_number = int(dic.get('view_number'))
        news_number = int(dic.get('news_number'))
        
        viewed_news = get_object_or_404(News, id=news_number)
        viewed_news.view_number += view_number
        viewed_news.save()
        return render(self.request, 'madridsite/news.html')

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
 
        context['check'] = Like.objects.filter(user=self.request.user)
        return context



    


def diagnosis(request):

    return render(request, 'madridsite/diagnosis.html')
def diagnosis_result(request):


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


class MyLikeView(ListView):
    template_name = 'madridsite/mylike.html'
    context_object_name = 'realnews'
    def get_queryset(self):
        # queryset = super(ListView, self).get_queryset()  
        queryset = Like.objects.filter(date_created__lte=timezone.now(),user=self.request.user).order_by('date_created')
        return queryset

@login_required
def comment(request,pk):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('post_detail', pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'madridsite/comment.html', {'form': form})