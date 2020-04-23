
from mypack.point import Point

def test_bound_instance_method():
    #  바운드 메서드 방식 -> 인스턴스로 직접 접근하는 방법
    p = Point()
    p.set_x(10) # self는 따로 지정하지 않는다.
    p.set_y(20)
    print(p.get_x(),p.get_y())



def test_unbound_instance_method():
    # 언바운드 메서드 방식 -> 클래스를 통한 우회 접근
    p = Point()
    Point.set_x(p,10)  # 우회 접근이므로 실제 객체의 주소를 전달
    Point.set_y(p,20)

    print(Point.get_x(p),Point.get_y(p))

def test_class_static_method():
    print(Point.static_method())



def test_lifecycle():
    p =Point()
    print(p,"instance_count{}".format(Point.instance_count))
    p2 = Point(10,20)
    print(p2,"instance_count{}".format(Point.instance_count))

    del p # 객체의 삭제 -> __del__ 실행
    print("instance_count{}".format(Point.instance_count))
    del p2
    print("instance_count{}".format(Point.instance_count))



def str_repr():
    p = Point(10,20)
    print(p,str(p))

    code = repr(p)
    print(code)

    # repr로 반환된 출력으로 객체를 다시 생성할 수 있어야 한다.
    repr_o = eval(code)
    print("재현된 객체:",repr_o,type(repr_o))

    print(" p == repr_o?", p ==repr_o)

    # __add__
    print("p+ Point:",p + Point(20,30))
    print("p+int:",p + 10)

    # __sub__
    print("p - Point:", p - Point(20, 30))
    print("p - int:", p - 10)









if __name__ == '__main__':
    # test_bound_instance_method()
    # test_unbound_instance_method()
    # test_lifecycle()
    str_repr()