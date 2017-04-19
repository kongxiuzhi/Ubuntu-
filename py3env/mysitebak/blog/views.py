from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.core.mail import send_mail
from .models import StaffIf,Post,OtherIf,Comment
from .forms import EmailPostForm,CommentForm



# Create your views here.
def index(request):
    kxz = StaffIf.objects.get(name="孔秀志")
    dy = StaffIf.objects.get(name="代洋")
    wy = StaffIf.objects.get(name="武岳")
    xyl = StaffIf.objects.get(name="许永亮")
    xck = StaffIf.objects.get(name="薛诚锴")
    wc = StaffIf.objects.get(name="吴超")
    zxw = StaffIf.objects.get(name="张晓伟")
    pdy = StaffIf.objects.get(name="彭登涯")
    
    #list comments
    comments = Comment.objects.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponseRedirect("/IT/")
    else:
        comment_form = CommentForm()


    context = {'kxz':kxz,'dy':dy,'wy':wy,'xyl':xyl,'xck':xck,'wc':wc,'zxw':zxw,'pdy':pdy,
               'comments':comments,'comment_form':comment_form} 
    templateshome = "blog/home.html"
    return render(request,templateshome,context)


#每个人的blog
def gerenblog(request,mingzi):
    a={'kxz':'孔秀志','dy':'代洋','pdy':'彭登涯','zxw':'张晓伟','wy':'武岳','wc':'吴超','xck':'薛诚锴','xyl':'许永亮'}
    infors= get_object_or_404(StaffIf,name=a[mingzi])
    posts = Post.published.filter(author=a[mingzi])
    content = {'infors':infors,'posts':posts}
    template = "blog/post/gerenblog.html"
    return render(request,template,content)


def service(request):
    objects_list = OtherIf.objects.all()
    return render(request,'blog/post/blank.html',{'otherif':objects_list})
#post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request,'blog/post/list.html',{'page':'page','posts':posts})

def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='发表',publish__year=year,publish__month=month,publish__day=day)
    infors= get_object_or_404(StaffIf,name=post.author)
    return render(request,'blog/post/detail.html',{'post':post,'infors':infors})


def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='发表')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'],
            cd['email'],post.title)
            message = 'Read "{}" at {}\n\n{}\'s comments:{}'.format(post.title,
            post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'kongxiuzhi@boe.com.cn',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,'form':form,'sent':sent})

def div_blog(request):
    return render(request,'blog/baseblog.html')
