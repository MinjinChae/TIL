# 1.

1) T

2) T

3) F -> related_name은 필요한 상황이 있지만 필수 인자는 아니다.



# 2.

(a) request.user

(b) articles.like_users.all()



# 3.

(a) user_pk

(b) followers

(c) filter

(d) remove

(e) add





# 4.

 AUTH_USER_MODEL을 settings.py에 등록해줬기 때문이다.

`settings.AUTHP_USER_MODEL` 를 작성해줘야 한다.





# 5.

like_users 필드 생성 시 역참조는 .articles_set 매니저를 생성하는데 User:Article의 관계에서 이미 해당 매니저의 이름을 사용 중이기 때문이다.





# 6.

(a) person.followings.all()

(b) person.followers.all()

(c) user

(d) person

(e) person.pk