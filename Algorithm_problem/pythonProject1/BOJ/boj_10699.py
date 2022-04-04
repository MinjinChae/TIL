# datetime 모듈
import datetime
# datetime.datetime date모듈과 time모듈의 조합
# -> year, month, day, hour, minute, second의 정보를 나타냄
# now() 함수 -> 지금의 날짜, 시간을 출력
# str() 함수 -> 출력하려는 내용을 string 형태로 출력
# [:10] 10글자만 출력하기 년,월,일
print(str(datetime.datetime.now())[:10])

