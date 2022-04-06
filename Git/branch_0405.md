branch를 쓰게 되면 서로 뭘 변경하든 신경 쓰지 않고 현재 상태에서 상대방에게 영향을 미치지 않고 나만의 길을 갈 수 있음! -> 현업에서 많이 사용함

브랜치: 특정 커밋을 가리키는 '포인터'

master branch

feature A

feature B

총 3개의 branch가 C4를 가르킴

featureA에서 작업할거야 선언을 하고 브랜치를 커밋을 처음 찍으면 분기가 되면서 A1 커밋이 찍힘 

featureB도 동일

포인터는 단 한개씩 존재함 



현재 우리 프로덕트는 master branch 위에 있음(소비자가 사용하고 있는 공간)

feature-B 새로운 기능을 개발하고 이걸 적용 시켜주기 위해서는 

feature-B가 가리키는 B2커밋과 마스터가 가리키는 C4 커밋을 합쳐서  M1 머지1을 만들고 master와 feature-b가 M1이라는 커밋을 가리키게함 우리의 프로덕트는 feature B가 개발한 기능을 반영해서 M1

feature A도 개발을 다하고 기능을 반영하려면 현재 마스터가 가리키는 M1이랑 featureA가 가리키는 A2랑 머지해서 feautre A랑 마스터가 새로운 커밋을 가리키게함



featureb를 지워도 포인터만 사라지지 히스토리는 지워지지 않음 -> 아무것도 일어나지 않아..



가리키던 merge를 슉 댕겨오는거 fast-forward 

conflict가 발생하면 무조건 merge commit case로 감





