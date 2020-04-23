# 심볼 테이블
g_a = "global"
def f():
    l_a = "local a"
    def g():
        # 함수, 클래스 등은 내부에 자신의 심볼 테이블을 가지고 있다.
        l_b = "local b"
        print("g의 로컬 영역:", locals())
        print(l_b, l_a, g_a)
        # 변수의 내용을 참조할 때 검색의 순서
        # local -> Enclosed -> global -> Builtin 영역 순으로

    g()



def test_symboltable():

    print("GLOBAL:", globals())
    print("g_a is in GLOBAL:", "g_a" in globals())
    print("l_a is in GLOBAL:", "l_a" in globals())
    f()

def object_id():
    lst1 = [1,2,3]
    lst2 = [1, 2, 3]
    lst3 = lst1

    print("lst1 ==lst2 ?:", lst1 == lst2)
    print("lst1 ==lst3 ?:", lst1 == lst3)

    print("Addr of lst1:",id(lst1))
    print("Addr of lst2:", id(lst2))

    print("lst1의 주소 == lst2 주소?", id(lst1) == id(lst2)) # 값은 같으나 다른 객체이다.
    print("lst1 is lst2?",lst1 is lst2 )
    # == : 값의 비교 (동질성 비교)
    # is : 주소의 비교 (동일성 비교)
    print("lst1 is lst3?", lst1 is lst3) # 두 객체는 같은 객체

def object_copy():
    a = [1,2,3]
    b = [4,5,a]
    x = [a,b,100]

    y = x # 참조 복사
    print(x,y)

    x[2] = 10
    print(x,y)

    # 방법1
    y = x[:]
    y=x.copy()
    import copy
    y = copy.copy(x)
    print("COPY:",x ,y)
    print("x is y ?", x is y)

    x[2] = 100
    print(x,y)

    y=x[:]
    print(x,y)
    print("x[0][0] is y[0][0] ? ", x[0][0] is y[0][0])
    x[0][0] = 10
    print(x,y)

    # 주의 : 복합 객체를 복제할 때는 말단의 요소들부터 복제해서 새로 객체를 재구성 필요
    # -> deepcopy
    y = copy.deepcopy(x)
    print("DEEPCOPY:", x, y)
    print("x[0][0] is y[0][0] ? ", x[0][0] is y[0][0])

    # 방법2




if __name__ == '__main__':
    #test_symboltable()
    #object_id()
    object_copy()



