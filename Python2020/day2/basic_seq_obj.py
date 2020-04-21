def range_ex():
    """
    범위 객체
    -range(경계)
    -range(start, end)
    -range(start, end, step)
    """
    seq = range(10)
    print(seq,type(seq))

    print(seq,"LENGTH:", len(seq))
    print("5 in seq:", 5 in seq)
    print("정인덱싱:",seq[0],seq[1],seq[2])
    print("역인덱싱:", seq[-1], seq[-2], seq[-3])
    print("슬라이싱:", seq[2:5])

    # range 객체를 이용 loop
    for num in range(2,10):
        print("num in range:",num)

def enumerate_ex():
    """
    순차형 loop시 추출된 값과 함께 값의 인덱스도 함께 필요할 때
    """
    words = "Life is too short, you need python".replace(",","").upper().split()
    print(words)

    # 기본 루프
    for word in words:
        print("word:",word)

    for index, word in enumerate(words):
        print("{}번째 단어 => {}".format(index,word))

def zip_ex():
    # 여러 시쿼스 자료형을 동시 같은 위치희 것을 묶어주는 객체
    # 시퀀스 자료들의 길이가 다를 때, 짧은 쪽을 맞춰진다.
    # 데이터를 추출하면 비어버린다.
    engs = [ "sunday", "monday", "tuesday","wednesday"]
    kors = "일요일 월요일 화요일 수요일 목요일 금요일".split()
    engkor = zip(engs, kors)

    print(engkor)

    for pair in engkor :
        print("pair:", pair)

        for eng,kor in engkor:
            print("Eng {} => kor {}".format(eng,kor))

    for index, (eng, kor) in enumerate(engkor):
        print("Eng {} => kor {}".format(eng, kor))


if __name__ == '__main__':
    #range_ex()
    #enumerate_ex()
    zip_ex()