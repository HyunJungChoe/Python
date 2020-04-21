def define_tuple():
    """
    튜플의 생성
    - 리스트와 거의 비슷, 불변 자료형
    """
    tp = tuple() # 공튜플
    print(tp, type(tp))
    # len, in, not in, 연결, 반복, 슬라이싱, 인덱싱
    # 불변 자료형 -> 슬라이싱 이용 치환 불가

    tp2 = ()
    tp3 = (1,)
    tp4 = (1,2,3)
    print(tp2, tp3, tp4)

def pack_unpack():
    """
    () 설정, () 없어도 튜플로 인식한다. -> packing
    """
    tp = (10, 20, 30, "python")
    tp2 = 10, 20,30, "python"
    print(tp,type(tp),tp2, type(tp2))

    (a, b, c, d)= tp2
    print(a,b,c,d)
    a2, b2, c2, d2 = tp # () 없어도 튜플
    print(a2,b2,c2,d2)

    # tp에서 첫 번째 요소만 추출
    x, *y = tp
    print(x, y)
    #tp 에서 마지막 요소만 추출
    *x, y = tp
    print(x,y)

    # tp에서 첫, 마지막 요소를 추출
    x, *y, z = tp
    print(x, y,z)

    #활용 : 함수에서 여러개의 값을 리턴할 수 있다.
    def multi_ret():
        return 10, 20, 30





if __name__ == '__main__':
    #define_tuple()
    pack_unpack()
   
