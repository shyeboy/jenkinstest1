from django.shortcuts import render


from .models import Post

def index(request):
    # 게시물 목록 출력
    postList = Post.objects.order_by('-date')
    context = {'postList': postList}
    return render(request, 'board/list.html', context)

def detail(request, postId):
    # 상세보기
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'board/detail.html', context)

def answer_create(request, postId):
    # 답글 추가
    post = get_object_or_404(Post, pk=postId)
    post.answer_set.create(content=request.POST.get('content'), date=timezone.now())
    return redirect('board:detail', postId=postId)
#Create your views here.
