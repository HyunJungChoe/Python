def define_set():
    """
    셋(집합) 자료형
    - 순서 없고 중복이 없는 자료, 가변 자료형
    - len, in, not in 정도만 가능
    """
    empty_set = set() # 빈 셋
    print(empty_set, type(empty_set))

    s1={1, 2, 3}
    print(s1,type(s1))

    # 타 자료형을 이용한 셋 만들기
    s="python programing"
    s2=set(s)
    print(s2,len(s2))

    # 중복없는 특성을 이용 -> 유일 값을 추출하는데 유용
    word  = "java programing python programing system programing".upper().split()
    s3=set(word)
    print("s3:", s3)

    # 길이
    print(s3,"LENGTH:", len(s3))
    print("PROGRAMING" in s3)

numbers = {0,1,2,3,4,5,6,7,8,9,10}
evens = {0,2,4,6,8,10}
odds = {1,3,5,7,9}
mthree = {3,6,9}

def set_methods():

    s =set()
    s.add(3)
    print("add:",s)
    s.update({3,6,9})
    print("update:",s)

    # 삭제
    s.discard(3)
    print("discard:",s)
    s.discard(3)
    if 3 in s:
        s.remove(3)
    else:
        print("3 not found")

    # 합집합
    print("짝수 합 홀수 : ", odds | evens)
    print("짝수 합 홀수 : ", odds.union(evens))
    print("짝수 합 홀수 == 전체 : ", odds|evens == numbers)

    # 교집합 & intersection
    print("홀수 교 3배수:", odds & mthree)
    print("홀수 교 3배수:", odds.intersection(mthree)=={3,9})

    # 차집합 : -, difference()
    print("전체 차 짝수:", numbers  - evens)
    print("전체 차 짝수 == 홀수 :", numbers.difference(evens)==odds)

    # 모집합과 부분집합의 확인
    print("짝수는 전체의 부분집합?",evens.issubset(numbers))
    print("전체는 짝수의 모집합?", numbers.issubset(evens))

    #
def loop():
    print("numbers:", numbers)

    for num in numbers:
        print(num)


if __name__ == '__main__':
    #define_set()
    #set_methods()
    loop()