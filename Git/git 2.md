레포지토리:커밋저장소

git init 로컬 레포지토리 생성

.git이라는 폴더가 생성이 되고 git이 관리하는 모든 정보가 여기 들어있음

이걸 지우면 안된다!! 이걸 지우면 레포지토리가 아닌 일반 폴더가 되버리는것..

git  명령어를 입력하고 나면 (master)가 생기고 이제부터 git으로 버전관리가 가능하게됨

git status 현재 레포지토레에 git이 어떤 상태인지 체크할 수 있음

README.md 내 레포지토리에 대한 설명서 같은 역할을 하는 파일

touch README.md README.md  파일을 생성함

이때 git status를 해보면 untracked files이라고 뜸 새로운 파일이 들어왔는데 이건 내가 추적하고 있지 않은 파일이야! 

git add Staging Area로 올리는 역할 git에게 추적하는 파일임을 선언

git add . 를 해서 모든 파일을 올릴 수 있음 

.은 현재 위치를 의미

git status 를 해보면 new file:~ 

git commit -m ""

please tell me who you are  커밋을 남기려면 너가 누군지 알려줘야해!

global 옵션은 한번 사용하면 더이상 안물어봄 (깃랩 깃헙 계정을 다르게 가지고 있으니까 추천X)

git config user.email ""

git config user.name ""

git commit 하면  CLI환경, Vim이라는 프로그램이 생성 여기서는 commit 메세지를 여러줄로 적을 수 있음

i를 누르면 insert라고 뜸 수정모드 이상태에서 이 파일을 수정하면 됨

맨윗줄에는 파일의 타이틀

그리고 한 줄 띄워주고 

최조 파일 init

프로젝트 설명서 작성 예정

두줄 띄워줌 

esc 누르면 insert 사라짐

맨 밑에  : wq 저장하고 나간다는 뜻

commit을 쓰고 나갈 수 있음

git log를 치고 내commit 확인

readme.md 파일을 수정하려면?

ls를 쳐서 확인하고 vi README.md를 하면 아까처럼 vi 프로그램에서 열림

i로 수정모드로 바꾸고 수정한 후 esc -> :wq 로 나감

수정했으니까 git status를 보면 이 파일이 modified 되어있음 (working directory)

이제 staging area repository에 올리면 됨

이제 local 과 remote 레포지토리를 연결해야함

github에서 레포지토리 생성하고 

git remote add origin url

remote 레포지토리를 추가를 해줄거야 그 이름은 origin url은 너무 기니까 origin이라는 이름을 붙여줌

 그다음에 로컬 레포지토리에 있는 작업상황들을 우리가 작업한 커밋들을 remote 레포지토리에 올릴거

그게바로 git push 명령어 맨처음 push를 할때는 u옵션을 줘야함 git push  -u origin master

set upstrem origin에다가 내 master branch를 push해줄거야하고 맨처음에 설정해줌

긴 url은 귀찮으니까 origin을 사용 큰 줄기에 있는 변경사항들을 origin에 push 할거야!

public 모든 사람이 볼 수 있고 다운 받을 수 있지만 push는 안됨 여기서 다운은 clone을 의미함

private 불 수도 없고 다운 받을 수도 없고 push도 나만

git은 협업을 위한 도구! 

github에서 test_co라는 새로운 레포지토리를 생성하고 git clone 을 하는데 이 경우에는 cd.. desktop에서 git clone 해줌 

touch REAEDME.md

git add .

git commit pleas tell me who you are

git config user.email "" 

git config user.name""

git commit -m ""

git log  commit생성된거 확인

이제 push해야하는데 이번에 git remote add가 필요할까?

아까전에는 local에서 레포지토리 먼저 만들고 remote repo의 url을 가져와서 연결했는데 이번에는 remote repo를 먼저 만들고 클론해서 local repo에 가져왔기 때문에   git remote add하는 과정이 필요없음 그래서 바로 git push 근데 여기에 git push (origin main)이 숨겨져 있는거

github

push 전에는 pull 이 있다...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!





