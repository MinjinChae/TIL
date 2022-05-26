장르 누르면 해당 장르 영화 리스트로 이동함

홈 접속할 때마다 바뀌는거



Home 

actor RV genre, actor, keyword, 검색image(actor)

장르 누르면 해당 배우의 해당 장르의 영화 추천

해당 장르 영화 추천

HomeV 2안, movie data



movie list

모든 영화 데이터 poster image title

장르 배우 poster image  title



movie detail

poster image  title release date overview(or naver url link)

wathch trailer -> youtube url 

director, director img, actor, actor img, 추천, 추천수



actor list

actor, actor img



actor detail

actor(name),  좋아요, 좋아요 수, actor img, keywords



signup

username password 1,2 google(v2) naver(v1)



login

uersname, password, 네이버로 로그인하기, 비번찾기



review list

title, 작성자, created_at



review detail

title content 작성자 created_at , img, 

ㄴ comment list content, 작성자,

​	ㄴcomment list form content (작성자) 





review new

title content img(선택사항)



review edit

value(title, content, img)





 

1.오늘한거

2.어려웠던점

3.해결한점



npm install lodash axios bootstrap

vu

npm i lodash axios bootstrap-vue

vuex-persistedstate

vue-bootstrap



 npm install 





프로젝트 생성 

vue create final-pjt-frontend

cd final-pjt-frontend

npm i lodash axios bootstrap-vue

vue add router 

vue add vuex

views component 만들어주기

store에 modules 폴더 만들어서 js 파일 나눠주고 index.js 

Navbar, Footer 만들고 

error!!!  Component name "Footer" should always be multi-word  vue/multi-word-component-names 



대소문자, 오타조심

로그인 필요해서 데이터가 안뜬거



이미지한테 wieth height 주고 width height 200px img 태그 옆에 div width height 100% relative, absoulute div display none img:hover + div.클래스명 { display: block } word-break: break-all



수정사항

footer 그냥 바이바이했음 헝

- movielist

  사진 위에 마우스 올리면 포인터로 변하기

  패딩 줘서 마우스 올렸을 때 첫번째 줄이 밑으로 내려가는거 고치기

  포스터 사이즈를 더 키울 수 있나?(더 키울 수 있으면 키우는걸루..)

  전체적인 마진,패딩

  폰트 스타일, 크기

- moviedetail

  네이버 영화 페이지로 가는 링크(a태그) 아직 안만들었음

  지금 그냥 iframe 넣었는데 역시 모달로 바꾸는게 더 이쁠듯..

  -> 근데 모달로 넣었을 때, 반응형 맞춰주는게 관건...ㅠ

  아직 데이터 안넣어봐서 고양이 이미지로 대체 -> 오 잘된당

  전체적인 마진, 패딩

  폰트 스타일, 크기

- actorlist



 python manage.py loaddata movies.json images.json genres.json directors.json actors.json



- moviedetail

  감독, 출연진 데이터 뽑아서 사진이랑 이름 배치 누르면 배우 디테일 페이지로 이동하도록 router 기능 추가!

- actorlist

  사진 배치, css효과 주기 이름 누르면 배우 디테일 페이지로 이동하도록 router 기능 추가하기

- actordetail 

  좋아요 기능이 이상하다...! ㅠㅠ

  배치 다시 시켜주기 

   word cloud or tag cloud 

- homeview

- community

- 404페이지로 이동하는거 수정!











