# 1) Read

![index](workshop_0310.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-10%20213431.jpg)



# 2) Create

![create](workshop_0310.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-10%20215126.jpg)



# 3) Detail

![detail](workshop_0310.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-10%20215105.jpg)



# 4) Update

![update](workshop_0310.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-10%20215126.jpg)





# urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', include('articles.urls')),
]
```





# articles/urls.py

```python
from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('index/', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
]
```





# views.py

```python
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:detail', article.pk)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {'article': article,}
    return render(request, 'articles/edit.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
```





# templates/articles/index.html

````html
{% extends 'base.html' %}

{% block content %}
  <h1 class="fw-bold">INDEX</h1>
  <a href={% url 'articles:new' %} class="btn btn-info">NEW</a>
  
  <hr>
  {% for article in articles %}
    <h2>제목: {{ article.title }}</h2>
    <p>내용: {{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk %}" class="btn btn-secondary">DETAIL</a>
    <hr>
  {% endfor %}

  
{% endblock content %}
````





# templates/articles/new.html

```html
{% extends 'base.html' %}

{% block content %}
<h1 class="fw-bold">NEW</h1>

<form action="{% url 'articles:create' %}" method="POST">
  {% csrf_token %}
  <label for="title">TITLE:</label>
  <input type="text" name="title" id="title"><br>

  <label for="content">CONTENT:</label>
  <textarea name="content" id="content" cols="30" rows="10"></textarea><br>

  <input type="submit" value="작성">
</form>

<a href={% url 'articles:index' %} class="btn btn-warning my-1">BACK</a>
{% endblock content %}
```





# templates/articles/detail.html

```html
{% extends 'base.html' %}
{% block content %}
  <h1 class="fw-bold">DETAIL</h1><hr>
  <h2>{{ article.title }}</h2>
  <p>{{ article.content }}</p><br>
  <p>{{ article.created_at }}</p>
  <p>{{ article.updated_at }}</p>
  
  <div class="d-flex">
    <a href={% url 'articles:edit' article.pk %} class="btn btn-primary m-1">EDIT</a>
    <form action={% url 'articles:delete' article.pk %} method="post">
    {% csrf_token %}  
    <button class="btn btn-danger m-1">DELETE</button>
    </form>
    <a href={% url 'articles:index' %} class="btn btn-warning m-1">BACK</a>
  </div><br>
  
{% endblock content %}
```





# templates/articles/edit.html

```html
{% extends 'base.html' %}

{% block content %}
<h1 class="fw-bold">EDIT</h1>

<form action="{% url 'articles:update' article.pk %}" method="POST">
  {% csrf_token %}
  <label for="title">TITLE:</label>
  <input type="text" name="title" id="title" value="{{ article.title }}"><br>

  <label for="content">CONTENT:</label>
  <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea><br>

  <input type="submit" value="수정">
</form>
<a href={% url 'articles:index' %} class="btn btn-warning my-1">BACK</a>
{% endblock content %}
```





# base.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
  <div class="container">
    {% block content %}
    {% endblock content %}   
  </div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```





# models.py

```python
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
```





