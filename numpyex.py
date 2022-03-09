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

print(np.linspace(0,2,9), '\n')       # 0부터 2까지 9번에 걸쳐 증가 : 즉 0.25씩 증가
                                # linspace는 마지막 요소를 포함한다. 즉 2를 포함한다.

# linspace의 활용처
x = np.linspace(0, 2*pi, 100)   #0부터 2pi까지 100개의 요소를 가지는 배열 생성
f = np.sin(x)                   #생성한 각가의 배열에 대해서 sin 값을 계산하여 대입
print(f, '\n')                        # 출력

# element-wise : minus
# np에 대한 연산은 element-wise하게 일어난다.
a = np.array([20,30,40,50])
b = np.arange(4)
c = a - b
print(c)
print(b**2)
print(a<35, '\n')


# 서로 다른 데이터타입 간의 연산

a = np.ones(3, dtype=np.int32)  # a는 int32 타입
b = np.linspace(0,pi,3)         # b는 float64 타입
c = a+b                         # 둘을 더하면 더 정밀하고 정확한 데이터 타입으로 연산 결과가 치환된다.
print(c, '\n')
d = np.exp(c*1j)                # exp는 exponential의 약자, 오일러 수 e의 x승을 계산해주는 함수
                                # 1j를 곱하였기 때문에 d의 데이터 타입은 complex128, 복소수가 된다.

# numeric operation with conditions

b = np.arange(12).reshape(3,4)
print(b.sum(axis=0))            # axis=0, 즉 각 열의 합을 출력한다.
print(b.min(axis=1))            # axis=1, 즉 각 행 중 최솟값을 출력한다.
print(b.cumsum(axis=1), '\n')         # 각 행의 왼쪽부터 누적합을 출력한다.


# indexing, slicing, iterating

a = np.arange(10)**3
print(a[2])
print(a[2:5])                   # slicing : 0부터 시작하니 2,3,4번 인덱스만 자른다.
a[:6:2] = -1000                 # 콜론이 앞에 붙으면 앞 인덱스까지 slicing을 하되 뒤 인덱스 만큼 건너뛰어라는 것을 의미
                                # 즉 여기에서는 5인덱스까지(6은 미포함이므로) 2칸씩 건너뛰며 슬라이싱하라는 의미.
print(a, '\n')
a[ : :-1]                       # 역순으로 출력

    # from function

def f(x,y):
    return x*10 + y

b = np.fromfunction(f,(5,4),dtype=int)  # 출력 결과가 이해가 안갈 수도 있는데, x값은 행의 인덱스, y값은 열의 인덱스라고
                                        # 생각하면 이해가 된다. 즉 (2,1)행의 값으로는 2*10 + 1 = 21이 들어간다.
print(b, '\n')

print(b[0:5, 1])                        # 행은 0번 index부터 4번 index까지, 열은 1번에 해당하는 요소들을 모두 출력한다.
#b[ : , 1] 과 위의 코드는 같은 의미이다.
print(b[1:3, : ])                       # 행은 1,2번 index, 모든 열에 해당하는 값을 출력한다. 출력된 값은 2d array이다.
print(b[-1], '\n')                      # 다차원인데 parameter가 하나만 전달된 경우 나머지 parameter들은 모두 :(콜론)이 들어간다.
                                        # -1은 가장 끝의 원소를 뜻함.

# iterator

for row in b:                           # 그냥 b로 입력되면 행 단위로 출력하는 것 같다.
    print(row)

for element in b.flat:
    print(element)                      # b.flat으로 입력되면 요소 하나하나를 출력한다.


# shape

a = np.floor(10*np.random.random((3,4)))    # floor는 매개변수로 전달된 값을 반내림? 하는 기능이다.
print(a)

print(a.ravel())                        # ravel은 array를 평평하게 펴서 return해준다.
print(a.flatten())                      # flatten도 마찬가지로 array를 평평하게 펴서 출력해준다.
                                        # 둘의 차이는 ravel은 얕은 복사, flatten은 깊은 복사이다. 즉 ravel은 변동사항이 원본 배열에 반영된다.
                                        # ravel은 새로운 메모리 공간은 필요 없어서 더 빠르지만 얕은 복사의 특성 상 특수한 경우에만 사용된다.
print(a.reshape(6,2))
print(a.reshape(3,-1))                  # 꿀팁 : reshape에서 사용되는 -1은 다른 매개변수들을 고려해서 가능한 사이즈를 자동으로 계산해준다.

# stacking arrays

a = np.floor(10*np.random.random(2,2))
b = np.floor(10*np.random.random(2,2))
print(np.vstack((a,b)), '\n')                   # a와 b를 수직 방향으로 쌓는다(stack)
print(np.hstack((a,b)), '\n')                   # a와 b를 수평 방향으로 쌓는다.