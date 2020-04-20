# 파이썬의 일반적인 뼈대

def do_nothing(): #블록의 시작
    pass  #내부 실행 내용 이 없더라도 비워두면 안됌.

def print_something():
    print("hello, Python")


def arith_oper():
    #산술 연산자
    print("7/3?", 7/3)
    print("7//3?", 7//3)
    print("7%3?", 7 % 3)

    # 나눗셈 몫과 나머지 함수
    print(divmod(7, 3))


def complex_ex():
    # 복소수 : 정수부 + 허수부
    c = 3+4j
    print(c) #복소수
    print(c.real) #실수부
    print(c.imag) #허수부
    print(c.conjugate()) #켤레복소수

def re1_oper():
    #관계 연산자 대소비교 -> 결과는 bool
    #데이터 타입의 대소 비교를 할 수 있다.
    print("abcd" < "abce")
    print((1, 2, 3) > (1, 2, 4))

def variable_ex():
    # 변수 연습
    # 명명 규칙 : 문자, 숫자, _의 조합. 단 숫자로 시작하면 안된다.
    import keyword #예약어 모듈
    print("예약어 목록 :", keyword.kwlist)
    print("예약어 갯수 :", len(keyword.kwlist))

    # 기본적인 할당
    a=2020
    print(a,type(a))
    print(a,"는 수치형인가?" ,isinstance(a,(int, float, complex)))

    #파이썬은 동적 타이핑 언어
    a="python"
    print(a, type(a))
    print(a, "는 문자형인가?", isinstance(a,str))

    # 여러 함수를 한번에 할당
    b, c, d = 10, 20 , 30
    print(b, c, d)

    # 같은 값 할당
    x=y=z= 10
    print(x,y,z)

    # 변수 swap
    e, f = 10, 20
    print("현재 ->",e,f)
    e,f = f,e # swap
    print("swap ->",e,f)

def logical_oper():
    # 논리연산 : 논리합 or , 논리곱 not , 논리 부정 not
    a= 7
    print(a,"는 0~10 사이?", a > 0 and a < 10)

    print(a, "는 0~10 사이?", 0< a < 10)

    b =13
    print(b,"0보다 작고 10보다 크다?", b <=0 or b >= 10)

    print(b,"0< b < 10", not( b <=0 or b >= 10))  #0< b < 10

if __name__ == "__main__":
    #do_nothing()
    #print_something()
    #arith_oper()
    #complex_ex()
    #re1_oper()
    #variable_ex()
    logical_oper()