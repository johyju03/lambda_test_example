from functools import reduce

# lambda 테스트
data = (lambda x, y: x + y)(10, 20)
print(data)

# map - lambda 조합 테스트
# python3 의 경우, map 함수 전에 list 로 감싸야 list 형태로 반환
data2 = list(map(lambda x: x + 10, range(0, 5)))
print(data2)

# reduce - lambda 조합 테스트
data3 = reduce(lambda x, y: x + y, range(0, 5))
print(data3)

# filter - lambda 조합 테스트
data4 = list(filter(lambda x: x > 5, range(3, 10)))
print(data4)
