Q1. 정적 웹 페이지 vs 동적 웹 페이지 



Q2. MVC vs MTV



Q3.MTV가 뭔데?



Q4. 가상환경 생성 부터 앱 생성까지 설명해봐



Q5. 앱 생성 후 뭐해야해? 



Q6. 사용자에게 제공하는 언어를 한국어로 바꾸려면?



Q6. 사용자에게 보여주는 시간을 한국 시간으로  바꾸려면?



Q7. DTL tag 반복문 쓰는 방법은? food로 해봐봐

{% for food in foods %}

{% endfor %}



Q8. base.html 안에 뭐 적어줘야해? (힌트: ex어쩌구랑 bl어쩌구)

{%extends 'base.html'%}

{% block content %}

{% endblock %}



Q9.템플릿 상속 받고나서 뭐 해야해?

BASE_DIR / 'templates'



Q10. url namespace를 해줘야 하는 이유랑 어떻게 해줘야해?  



Q11. template namespace를 해줘야 하는 이유랑 어떻게 해줘야해?



Q12. static 태그 적는 법(이미지 넣어봐봐)

{% load static %}

<img src={% static '~~'%}



Q13.  model이 뭐야



Q14. CharField랑 TextField 차이점 뭐게 ㅠㅠㅠ

class Article(models.Model):

​	title = models.CharField(max_length=10)

​	content = models.TextField()

​	created_at = models.DateTimeField(atuo_now_add=True)

​	updated_at = models.DateTimeField(auto_now=True)



Q15. migraitons 명령어 다 써봐 각각 역할 뭐게 ㅠㅠㅠ

python manage.py makemigrations 

python manage.py migrate

python manage.py sqlmigrate app_name 0001

python manage.py showmigrations



Q16. auto_now_add랑 auto_now 차이점 뭐게



Q17. create하는 3가지 방법(코드 적어봐 article을 예로!)

article = Article()

article.title='제목1'

artilcle.content='내용이야'

article.save()



article = Article(title='제목22', contnet='내용이다')

article.save()



Article.objects.create(title='제목3', content='내용이다ㅏ다다')



Q18. read하는 3가지 방법(코드 적어봐 article을 예로!)

전체 조회

Article.objects.all()

get

Article.objects.get(id=1)

filter

Article.objects.filter(content='django')



Q19. content에 ja가 포함하는 데이터 조회해봐

Article.objects.filter(content__contains='ja')

Q20. id가 2인 데이터 조회해봐





Q21. id가 2인 데이터 조회해서 title을 'byebye'로 바꿔봐

article= Article.objects.get(id=2)

article.title='byebye'

article.save()

Q22. id가 2인 데이터를 지워봐

article.delete()

Q23. object가 사람이 읽을 수 있는 문자열로 반환하기 위해서 class밑에 어떤 method를 써야해?

def~부터 적어봐!

def \__str__(self):

​	return self.title



Q24. admin 생성 명령문은?

python manage.py createsuperuser



Q25. admin 등록할 때 코드 적어봐

from .models import Article

admin.site.register('Article')



Q26. 게시글 정렬 순서 변경하는 방법 2가지랑 차이점 뭐게

Article.objects.all()[::-1]

Article.objects.order_by('-pk')



Q27. GET vs POST 



Q28. csrf token 태그를 코드로 적어봐, 언제 쓰는데?

{% csrf_token %} 



기억해!! import해줘야 하는것 ? include random view redirect  



foods 리스트가 있고

숫자만 출력하고 

{% for food in foods %}

\<p>{{ forloop.counter }}번째  음식:{food}\</p>

{% endfor %}











