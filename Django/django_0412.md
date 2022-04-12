장고는 기본적으로 유저라는 테이블을 만들어 놓고 사용함

회원가입 버튼을 누르면 당연히 form이겠지? form에 회원가입 정보를 입력하고 누르면 포스트 방식으로 우리에게 데이터가 들어오는게 있을거고 처음 회원가입하려고 링크를 눌렸을때 우리는 빈 폼을 보여주면 됨(이건 GET방식)



패스워드를 암호화해서 DB에 저장한거

장고는 짱이야...

valid_password method 비밀번호에 관한 유효성 검사를 할 수 있는 method가 있음

유저네임이랑 비슷하면 ㄴㄴ 적어도 8자 이상 이런거



AuthenticationForm

로그인할 때 쓰는 form



UserCreationForm은 request를 안받는데 AuthenticationForm은 request를 인자로 받는거?

쿠키랑 세션때문에? 



middleware

reuqest.user라는 객체를 추가해줌

request.user가 로그인이 되지않은 상태면 세션이 없는 상태면 쿠키에 세션 id가 없는 상태면

어나미어쩌구

세션이 있는 상태면 해당 객체에 정보를 담고 있는 것



context를 넘겨준적이 없는데 어떻게 index 템플릿에서 .auth~가 되는거지..?

이걸 middleware가 해줌



next~

너 로그인하면 자동으로 여기로 이동해 이걸 쿼리스트링에 담아둔거!

 login_required를 쓰면 accounts/login/ -> 디폴트

HTTP는 어떠한 상태를 기억을 못해

login  페이지 보고 어디로 가야할지 기억을 해야하기  때문에 쿼리스트링에서 next=~ 하는거



이게 싫으면 settigs에 지정할 수 있음



delete할 때 int:pk 안해도되는 이유는 우리의 request 객체 안에 이미 user라는 정보가 들어있기 때문에 

update도 request안에 user가 들어있기 때문에 int pk 필요 없어



우리의 프로젝트에 사용하는걸 settings에 명시를 해주고 get_user_model 함수를 사용해줌

앞으로는 User~ 라는 모델을 커스터마이징해서 쓸거야

근데 이름이 똑같아서 참조못해

나는 settings에 적혀있는 Auth_user_ = ""

현재 내 프로젝트에 활성화 되어있는 유저 모델은 여기만  참조할거야



/accounts/password/

자동으로 설정되어있는 url