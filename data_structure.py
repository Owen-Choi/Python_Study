# stack

a = [1,2,3,4,5]
a.pop()
a.append(6)
print(a)

#queue

a.pop(0)
a.append(7)
print(a)

# tuple
# tuple은 값의 변경이 불가능한 list

b = (1,2,3,4,5)
# b.append(6)은 에러를 발생시킨다. 값의 변경이 불가능하므로
print(b*2)

# set
# set은 중복을 허용하지 않는 자료구조

s = set([1,2,3,4,1,2])
print(s)
s.add(5)
string_ex = "Hello world!"
string_to_list = list(string_ex)     # 문자열의 list화
string_to_set = set(string_ex)       # 문자열의 set화
print(string_to_list)
print(string_to_set)                 # 순서는 없지만 중복이 제거된 채로 출력되게 된다.