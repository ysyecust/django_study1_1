from django.shortcuts import get_object_or_404,render_to_response

from .models import Article

# Create your views here.
def article_detail(request,article_id):
    article = get_object_or_404(Article,id=article_id)
    context = {}
    context['article_obj']=article
    return render_to_response("article_detail.html",context)
def article_list(request):
    #articles = Article.objects.all()
    articles = Article.objects.filter(is_deleted=False)
    context = {}
    context['articles'] = articles
    return render_to_response("article_list.html",context)
'''
    try:
        article = Article.objects.get(id=article_id)
        context = {}
        context['article_obj']=article
        return render(request,"article_detail.html",context)
    except Article.DoesNotExist:
        raise Http404("not exit")
    #return HttpResponse("<h2>文章标题：%s</h2><br> 文章内容：%s" % (article_id,article.content))
'''