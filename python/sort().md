# sort()

1. 딕셔너리의 경우  value값을 기준으로 정렬이 가능하다. 

2. 오름차순과 내림차순으로 정렬이 가능하다.

   -> 처음에 오름차순으로 정렬하고 평점이 낮은 영화들이 나와서 당황했다. 맨 뒤에서 슬라이싱 해줄까 생각했지만 reverse = True만으로 내림차순으로 정렬이 가능하다는 것을 알게 되었다! (이거 진짜 몰랐던 건데 유용하다!! 신기해!!)

   ```python
   # value값을 기준으로 정렬
   a_list = sorted(a_list, key = (lambda x : x ['key']))
   # 오름차순 정렬
   sorted(a, key = lambda x : x[0])
   # 내림차순 정렬
   sorted(a, key = lambda x : -x[0]) 
   sorted(a, key = lambda x : x[0], reverse = True)
   ```

    