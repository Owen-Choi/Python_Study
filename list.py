cities = ["서울","부산", "인천", "대구", "대전", "광주", "울산", "수원"]
color = ["yellow", "green", "black"]
color2 = ["orange", "white", "red"]

print(color + color2)
print(color * 2) # color 리스트가 2번 출력됨

color.append("gold")
color.extend(color2)
del color[0]
color.insert(0, "brown")
print(color)

orange, white, red = color2     # unpacking이라고 한다. 말도 안돼
print(orange, white, red)

print(cities[0:6])
print(cities[:])
print(cities[::2], " AND ", cities[::-1])
print("서울" in cities)
print("창원" in cities)

