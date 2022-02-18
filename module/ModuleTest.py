import CalcModule

# CalcModule을 import만 했을 뿐인데 모듈이 실행되어 원치않는 결과를 얻게된다.
# 이를 막기 위해서 모듈 내부에 if __name__ == "__main__": 를 추가해준다.
# 위 조건문의 역할은 말 그대로 메인 함수에서만 실행되는 것.
# 조건문을 모듈에 추가하면 더 이상 이 코드를 실행했을 때 모듈이 실행되지 않는다.
print("hello")