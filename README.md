### Lambda 함수 테스트용 예제 코드
***
- lambda 기본 예제
```python
data = (lambda x, y: x + y)(10, 20)
print(data)
# 결과 : 30
```
-  map - lambda 조합 기본예제 
```python
data2 = list(map(lambda x: x + 10, range(0, 5)))
print(data2)
# 결과 : [10, 11, 12, 13, 14]
```
* reduce - lambda 조합 기본예제
```python
from functools import reduce
data3 = reduce(lambda x, y: x + y, range(0, 5))
print(data3)
# 결과 : 10
```
* filter - lambda 조합 기본예제
```python
data4 = list(filter(lambda x: x > 5, range(3, 10)))
print(data4)
# 결과 : [6, 7, 8, 9]
```


 