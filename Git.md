Unix Linux는 같은 계열

CLI command line interface 검정색화면 ex.명령프롬포트

GUI graphic user interface  우리가 보는 화면

unix linux 명령어가 명령프롬포트에서는 지원되지 않음

window power shell은 일부 지원됨



###  간단한 Unix Linux 명령어

현재 위치의 폴더,파일 목록보기 ls

현재 위치 이동하기 cd\<path>

​                                 cd.. 상위 폴더로 이동

폴더 만들기 mkdir\<name>

*git bash를 열었을때 ~는 home디렉터리를 의미함

파일 만들기 touch\<name>

파일 삭제하기 rm\<name> 

폴더 삭제하기 rm -r\<name>



git bash ssafy파일에서  code . 을 입력하면  vsstudio가 켜짐

README.md 프로젝트 설명서

Repository 특정 디렉토리를 버전 관리하는 저장소

git init 로컬 저장소 생성 

git은 모든 히스토리가 들어있음 -> 버전 관리에 필요한 모든 것이 들어있음!

특정 버전으로 남기는것을 커밋(commit)한다 라고 

Working Directory/ Staging Area /Repository 3가지 영역을 바탕으로 동작함

1.Working Directory 내가 작업하고 있는 실제 디렉토리 ex) RacingGround     

untracked  git으로부터 추적받지 않음 ex) README.md  Basic.py

2.Staging Area 커밋으로 남기고 싶은 특정 버전으로 관리하고 싶은 파일이 있는 곳

tracked git git add되어서 이전 사항과 비교해서 변경 사항들을 Staging Area에 올림  staged가 됨

3.Repository 커밋들이 저장되는 곳 .git

git commit하면 commit01 1번의 Working Directory는 modified

이 동작을 반복하면 commit01 commit02 commit03...이 생성됨



git status 현재 git으로 관리되고 있는 파일들의 상태를 알 수 있음

git add. 추적 되지 않은 모든 파일과 추적 하고 있는 파일 중 수정 된 파일을 모두  Staging Area 에 올림

. 은 현재위치라는 의미를 가지고 있음 

.. 한칸 위에 부모 디렉토리 ex)cd..

git commit -m "commit_message" 커밋 메세지는 자세하게! ex)변수를 추가했음 



commit  을 main이라는 branh로 체크된 상태로 commit changes누름 

remote레지토리를 등록한 후에 u를 씀 

cd desktop

mkdir test

cd test

git init git으로 버전관리해줌

touch readme.md

git status 상태가 어떤 상태인지 

git add . 모든 변경사항을 한번에 

git statsus  

git commit -m "init"

please tell me who you are 

git config user.email ""

git config user.name "" 

git commit -m "init"

git log 지금까지 작성된 commit을 볼 수 있음

local에서는 끝

어딘가로 push하려면 remote 레포지토리가 필요

repo 를 연결하는 두가지방법

1. git clone 작업해서  add-commit-push

2. git init-git remote add origin{주소}-git pull origin branch

   git push -u origin master 맨처음 한번만 u옵션 필요

   

   1번 방법을 쓰자!

   클론 누르고 복사해서 git.clone 

   cd.. 

   desktop위치에 git clone url

   gitbub에서 remote 레포지토리가져와서 

   git add .

   git commit -m ""

   git push 

   

1.github에서 TIL_TEST  repo 생성

2.Local clone 받기

3.README.md 만들기 

4.add,commit  

5.push



### 정리

git 

분산 버전 관리 시스템 

하나가 이상 복구할 수 있음

하나의 파일을 여러가지 버전으로 만들고 그 버전은 버전 데이터베이스에 저장되어 있음 

데어터베이스=은행 

변경 사항만을 저장?? 이전 히스토리랑 비교해서 이전에는 무슨 작업을 했는지만 저장

뭐가 좋을까? 속도도 빠르고 저장용량도 줄고 모든면에서 효율적임



날아가도 다른곳에 저장되어있기 때문에 복구가 가능함 그래서 분산형이 좋은거

버전관리를 하는건 git

git을 이용해 버전관리된 데이터들을 관리해주는건 github

gitlab은 자기가 서버를 구축하는게 가능해서 싸피에서는 gitlab을 사용함

git은 분산 버전 관리 시스템 github는 git 기반의 저장소 서비스 이므로 둘은 다르다!

git bash ssafy파일에서  code . 을 입력하면  vsstudio가 켜짐



README.md 프로젝트 설명서

Repository 특정 디렉토리를 버전 관리하는 저장소

git init 로컬 저장소 생성 

git은 모든 히스토리가 들어있음 -> 버전 관리에 필요한 모든 것이 들어있음!

특정 버전으로 남기는것을 커밋(commit)한다 라고 

Working Directory/ Staging Area /Repository 3가지 영역을 바탕으로 동작함

1.Working Directory 내가 작업하고 있는 실제 디렉토리 ex) RacingGround     

untracked  git으로부터 추적받지 않음 ex) README.md  Basic.py

2.Staging Area 커밋으로 남기고 싶은 특정 버전으로 관리하고 싶은 파일이 있는 곳

tracked git git add되어서 이전 사항과 비교해서 변경 사항들을 Staging Area에 올림 

3.Repository 커밋들이 저장되는 곳 .git

