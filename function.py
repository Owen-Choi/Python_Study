def calculate(x, y) :
    print("returning rectangle area")
    return x * y

def power(x, y) :
    return x ** y   # x를 y제곱한 수

def spam(eggs) :
    eggs.append(1)  # ham의 주소에 append를 수행하였기 때문에 기존 ham에 1이 추가가 되게 된다.
    print(ham)
    eggs = [2,3]    # eggs에 새로운 주소를 할당했으므로 더 이상 이전의 ham이 아니다.
    print(eggs)

def f() :
    global s        # 전역변수를 그대로 사용하겠다는 의미
    s = "I love London"

x = int(input("please enter the x value : "))
y = int(input("please enter the y value : "))
print(calculate(x,y))
print(power(x, y))
ham = [0]
spam(ham)
print(ham)          # 결과는 함수에서 메모리 주소가 바뀌기 전 수정한 곳 까지 출력이 된다.

s = "I love Paris"
print(s)
f()
print(s)            # global 변수의 사용으로 인해 이 출력문의 결과는 함수 내부에서 바뀐 결과로 출력이 된다.