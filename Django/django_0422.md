many to many field는 어디에 작성해도 영향이 없음 

models.py에 class 정의 후 makemigrations, migrate

django seed 넣어주기

python manage.py django articles --number=10 

serializers.py 에서 모듈을 나눌 필요가 있음

articles에서 serializers 폴더를 만들고  모듈의 이름에 맞춰 serializer를 나눠줌

-> article.py /card.py /comment.py

article.py

from ..models import Article

from .comment imoprt CommentSerializer



views.py의 serializers import 부분은 잠시 주석처리

 

urls.py 

카드에 관해 조회할 수 있는 url 추가

path 추가

views.py 

serializer import해주는 부분 수정해주기

현재 디렉토리의 serializer의 article에서 serializer import

현재 디렉토리의 serializer의 article에서

현재 디렉토리의 serializer의 article에서



전체 카드에 대한 serializer조회 해주기



Article Detail에도 card에 대한 정보가 필요하다면 cardserializer를 별도로 import 해와서 넣어줘야함



card detail도 만들어주자





스웨거 설계화를 도와주는 대형 어쩌구 시스템이요..?ㅠㅠ

스웨거의 지원이 종료되면서 drf-ysag 