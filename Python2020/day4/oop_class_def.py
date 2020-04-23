# 클래스 -> 새로운 데이터 객체의 설계도
class MyClass:  # 설계도
    pass



# 인스턴스화
o= MyClass()
print(o,type(o))
# 부모의 확인
print("o의 부모클래스:",MyClass.__base__)
# 모든 객체의 부모는 object
print("오브젝트의 구성 요소들:", dir(object))

print("o는 어떤 클래스?",o.__class__)


# 상속 : 다른 클래스의 멤버를 물려받아 그대로 사용하는 것
class MyString(str): # 부모는 str 클래스
    pass

s = MyString("python programing")
print("MyString 의 부모 :", MyString.__base__)

# MyString 객체는 str의 모든 기능을 사용할 수 있다.
print(s.upper())
print(s.split())






