
def if_statement():
    # if~elif~else
    # 급액 입력
    # 10000원 이상 text, 2000원 이상 bus, 아니면 ,on foot

    money = int(input("얼마 가지고 있어?"))

    message = ""
    if money >= 10000:
        message = "Taxi"
    elif money >= 2000:
        message = "Bus"
    else:
        message = "On foot"

    print("이동방법:", message)

def if_expr():
    # if 표현식
    # 다른 연산 안쪽에 포함될 수 있다.
    money = int(input("얼마 가지고 있어?"))
    message = "Taxi" if money >= 10000 else "bus" if money >= 2000 else "on foot"
    print("이동방법:", message)


def list_comp():
    # syntax : 표현식 for 항목 in 순차형 if 조건

    a =[3,8,4,2,1,8,10,12]
    # for 문을 이용, 내부 값을 제곱.
    result =[]

    for num in a:
        result.append(num ** 2)
    else :
        print("Loop 정상 종료")
    print("result:", result)

    # 리스트 내포
    result2 =[num ** 2 for num in a]
    print("result2:", result2)

    # 리스트에서 짝수만 추출하여 새 리스트 생성
    evens = [num for num in a if num % 2 ==0]
    print("짝수 리스트:",evens)

    words = "a as bat cat dove tiger lion".split() # list
    print("words:", words)

    # 단어 목록 중에서 단어의 길이가 3 글자 이상인 단어의 목록
    result3 = [word.upper() for word in words if len(word) >= 3]
    print("단어 목록:",result3)

def set_dict_comp():
    # set
    # syntax: : { 표현식 for 변수 in 순차형 if 조건 }

    words = "a as bat cat dove tiger lion".split()  # list
    print("words:", words)
    # 단어 길이의 셋
    len_s = {len(word) for word in words}
    print("단어 길이 셋:", len_s)

    # dict
    # syntax: { 키표현식: 값표현식 for 변수 in 순차형 if 조건 }
    # 키-대문자 단어, 값-단어의 길이
    len_d = { word.upper:len(word) for word in words}
    print("단어 길이 사전:", len_d)



if __name__ == '__main__':
    #if_statement()
    #if_expr()
    #list_comp()
    set_dict_comp()