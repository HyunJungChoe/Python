def define_dict():
    """
    사전 정의 연습
    - 순서 없음, len, in, not in 활용
    """
    dct = dict()
    print(dct, type(dct))

    # 방법 2
    dct2 = {"basketball":5, "baseball:":9}
    print(dct2, type(dct2))

    # 내부데이터 접근
    print("key-basketball:", dct2['basketball'])
    #print("key-volleyball(없는키):", dct2['volleyball']) # 참조시 키가 없을 때 오류
    dct2["volleyball"] = 6
    # 길이 확인
    print(dct2,"LENGTH:",len(dct2))
    #포함 여부 확인
    print("volleyball in dct2?", "volleyball" in dct2)
    print("6 in dct2?",6 in dct2)

    # 생성 방법3. 키워드 인자를 이용한 사전 생성
    dct3 = dict(one =1 , two=2, three = 3)
    print(dct,type(dct3))

    # 생성 방법4. (키, 값)의 목록으로 생성
    dct4 = dict([("one",1),("two",2),("three",3)])
    print(dct4,type(dct4))

    # 생성 방법5. 키의 목록과 값의 목록이 따로 있을 때
    keys  =[ "one","two", "three"]
    values =[1,2,3]
    dct5 = dict(zip(keys,values))
    print(dct5,type(dct5))

dct = {
    "soccer": 11 , "baseball":9, "basketball":5
}

def dict_methods():
    print("soccer in dct?", "soccer" in dct)
    keys = dct.keys()
    print("keys:", keys,list(keys))
    values = dct.values() #값의 목록
    print("values:",values)
    #데이터가 값 중에 포함되어 있는가?
    print("9 in dct values?",9 in dct.values())
    items=dct.items()
    print("items:",items)

    # 키를 이용한 사전 내 값의 참조  : 키 접근 vs get






if __name__ == '__main__':
    #define_dict()
    dict_methods()

