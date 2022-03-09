import numpy as np
from numpy import pi

# shape : arange
print(np.arange(15).reshape(3,5))
print(np.arange(10000).reshape(100,100))    # 사이즈가 너무 클 경우 numpy에서 자동으로 중간을 생략하고 처음과 끝 부분만 보여준다.

print(np.zeros((3,4)))

# sequence : arange
print(np.arange(10,35,5))
print(np.arange(0,2,0.3))

# sequence : linspace

print(np.linspace(0,2,9))       # 0부터 2까지 9번에 걸쳐 증가 : 즉 0.25씩 증가
                                # linspace는 마지막 요소를 포함한다. 즉 2를 포함한다.

# linspace의 활용처
x = np.linspace(0, 2*pi, 100)   #0부터 2pi까지 100개의 요소를 가지는 배열 생성
f = np.sin(x)                   #생성한 각가의 배열에 대해서 sin 값을 계산하여 대입
print(f)                        # 출력

# element-wise : minus
# np에 대한 연산은 element-wise하게 일어난다.
a = np.array([20,30,40,50])
b = np.arange(4)
c = a - b
print(c)
print(b**2)
print(a<35)


# 서로 다른 데이터타입 간의 연산

a = np.ones(3, dtype=np.int32)  # a는 int32 타입
b = np.linspace(0,pi,3)         # b는 float64 타입
c = a+b                         # 둘을 더하면 더 정밀하고 정확한 데이터 타입으로 연산 결과가 치환된다.
print(c)
d = np.exp(c*1j)                # exp는 exponential의 약자, 오일러 수 e의 x승을 계산해주는 함수
                                # 1j를 곱하였기 때문에 d의 데이터 타입은 complex128, 복소수가 된다.

# numeric operation with conditions

b = np.arange(12).reshape(3,4)
print(b.sum(axis=0))            # axis=0, 즉 각 열의 합을 출력한다.
print(b.min(axis=1))            # axis=1, 즉 각 행 중 최솟값을 출력한다.
print(b.cumsum(axis=1))         # 각 행의 왼쪽부터 누적합을 출력한다.

