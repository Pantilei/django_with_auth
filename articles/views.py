from django.shortcuts import render, redirect
from articles.models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    print('Begining')
    if request.method == 'POST':
        # we create an instance of class CreateArticle the forms and give it the values from POST request. All of it are assigned to form variable
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            print(form)
            # save  in data base
            # commit=False means hang on a minute, we are gonna save this in a second but dont commite the action just yet. The instance that we are about to save,we will do something with it , then we will save it
            instance = form.save(commit=False)
            print(instance)
            print('Hello')
            # asigns the author atribute of object instance the loged user name
            instance.author = request.user
            print(instance.author)
            instance.save()  # we save in database with author atacched

            return redirect('articles:list')
    else:
        form = forms.CreateArticle()  # if we just need an empty page, GET request is made

    return render(request, 'articles/article_create.html', {'form': form})
