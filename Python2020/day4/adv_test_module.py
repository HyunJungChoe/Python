# sys 모듈 : 파이썬 인터프리터 관련 모듈
import sys
def test_sys():
    print(sys.platform)
    print(sys.version)

    args = sys.argv()
    args = args[1:]
    print(args)

import random
def test_random():
    # 랜덤 모듈
    # random.seed(42) # 재현성 확보를 위한 난수 초깃값
    # 개발 끝나면 없애자.
    print("0~1사이의 난수:",random.random())
    print("0~6사이의정수 난수:",random.randint(1,6))
    print("1~100, 간격 3 범위 난수:",random.randrange(1,101,3))

    # 순차형 지원 난수
    seq = ["짜장","짬뽕","짬짜면"]
    random.shuffle(seq)
    print("순차형 섞기:", seq)
    item = random.choice(seq)
    print("임의의 요소:",item)

    # 샘플링 :  모집합에서 포본집합 추출
    r = range(1,100000)
    print("샘플링:", random.sample(r,100))

    # 파이썬 내장 랜덤은 기본적인 상황에서의 난수 발생
    # 통계 기반 랜덤은 numpy.random 사용
    




if __name__ == '__main__':
    # test_sys()
    test_random()