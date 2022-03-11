git init 하면 (master)

하나의 작업은 하나의 branch에서 이뤄짐 독립적인 공간이기 때문에 수정 작업을 하면 master에 영향을 끼치지 않음! 

git branch:  브랜치 목록 확인

git branch 브랜치 이름: 새로운 브랜치 생성

git btanch -d 브랜치 이름: 특정 브랜치 생성(병합된 브랜치만 삭제)

git branch -D 브랜치 이름: 강제삭제

git log --oneline: git log를 한 줄로 볼 수 있음

git switch 브랜치 이름: 다른 브랜치로 이동

git switch -c 브랜치 이름: 브랜치를 새로 생성과 동치에 이동

git log --oneline --all: 전체 log가 보고싶을때

git log --oneline--all --graph: 가지가 갈라진걸 볼 수 있음



git switch를 할때는 모든 워킹 디렉토리에 버전 관리가 되고 있는지 확인해야함

add를 안한상태로 git switch를 해버리면 파일이 꼬임

merge(병합)

git merge 병합할 브랜치 이름

merge하기 전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 switch 해야 함

fast-forward 

3-way merge(merge-commit)

merge가 되면  그 브랜치는 역할이 끝났으니까 지워줌

merge conflict 

merge 하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하고 merge하면 git은 해당 부분을 자동으로 merge 해주지 못함

반면 동일 파일이더라도 서로 다른 부분을 수정했다면 conflict 없이 자동으로 merge commit 됨

