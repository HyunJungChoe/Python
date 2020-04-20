def bool_ex():
    b1 = True
    print(b1, "->", type(b1))
    print(b1, "bool?",isinstance(b1, bool))
    print(b1, "int?", isinstance(b1, int))

    print(bool(10),bool(0))
    print(bool("python"),bool(""))
    print(bool([1,2,3]), bool([]))
    print(bool(None))

def int_ex():
    d = 2020  # 10진수
    b = 0b1101 # 2진수 0b
    o = 0o23 # 8진수 0o
    x = 0xFF # 16진수 0x

    print(d, b, o ,x)
    print(bin(b),oct(o),hex(x))

def float_ex():
    a = 3.0
    b = 3.141592

    print(a,"float?", type(a), isinstance(a,float))
    print(b, "float?", type(b), isinstance(b, float))

    # 형태 판별 메서드
    print(a,"는 정수 형태? ", a.is_integer())
    print(b, "는 정수 형태? ", b.is_integer())

    # 지수 표기법 : e or E
    c = 3e3 # 3* 10 **3
    d = -2E-4 #


def casting_ex():
    a = "2020"
    b = 3.141592

    print(int(a), type(int(a)))
    c = "2020y" # 형태가 정수형이 아닌 데이터는 캐스팅할 수 없다.
    print(int(b),type(int(b)))

if __name__ == "__main__":
    #bool_ex()
    #int_ex()
    #float_ex()
    casting_ex()

