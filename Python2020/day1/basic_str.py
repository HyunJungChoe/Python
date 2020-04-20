def define_str():
    """
    문자열 선언 연습
    """
    s1 = "hello, python"
    s2 = str(3.141592)

    print(s1, type(s1), s2, type(s2))


    # """ 또는 ''' 여러줄 문자열
    # \ 를 사용하면 문장이 안 끝났음을 명시.

    s3 = """\
    여러줄 문자열
    만들 수 있음
    """
    print(s3)

def str_oper():
    """
    문자열 연산 -> 시퀀스 자료형 연습

    """
    # 문자열은 시퀀스 자료형, 불변자료형
    # len, in, not in
    # 슬라이싱, 인덱싱 가능

    s = "python"
    print(s,"LENGTH:", len(s))
    print("t가 내부에 있는가?","t" in s)

    #인덱싱
    print(s[0], s[1], s[2], s[3])
    print(s[-6], s[-5], s[-4], s[-3])
    print("가장 마지막 글자:",s[len(s)-1], s[-1])

    #슬라이싱 [시작 : 끝 경계], [시작:끝 경계: 간격] -> 경계값 설정에 유의
    print("th in s:", s[2:4])
    print("pyt in s:", s[0:3], s[:3])

    cp = s[:]  # 전체 문자열 복사
    print("복제본:",cp)

    print("s 간격 2:", s[::2])
    print(s[::-1]== "nohtyp")

    print("pyt"+"hon")
    print("ha"*3)

def search_methods():
    s= "I Like python, I Like Java"

    print("CNT:", s.count("Like"))

    i = s.find("Like")
    print("1st find:", i)
    i = s.find("Like", i + 4) #두번째 인자
    print("2nd find:",i)
    i = s.find("Like", i+4)
    print("3rd find:",i) # 없으면 -1

    #index 검색
    if "Like" in s[18:]:
        i =s.index("Like",18)
    else:
        print("Not Found")

    #역방향 검색: rfind, rindex
    i = s.rfind("Like")
    print("1st rfind:", i)
    i = s.rfind("Like",0, i)
    print("2nd rfind:", i)
    i = s.rfind("Like",0,i)
    print("3rd rfind:", i)

def modify_and_replace():
    # 편집과 치환 메서드들
    s = "   Alice and the Heart Queen   "
    print("STRIP:[",s.strip(),"]",sep="")
    s = "========Alice and the Heart Queen======="
    print("STRIP:[",s.strip("="),"]",sep="")

    print("STRIP and REPLACE:",s.strip("=").replace("Heart","Spade"))


def split_join_methods():
    s = "Ham and cheese and breads and cheese"
    print("split:", s.split())
    print("split( and ):", s.split(" and "))
    ingr = s.split(" and ")

    print("split 2개:", s.split(" and ", 2)) # and 기준 2개 왼쪽에서 추출
    print("rsplit 2개:", s.rsplit(" and ", 2))  # and 기준 2개 오른쪽에서 추출

    # join : 합치기
    ingr = s.split(" and ")
    print("재료 목록:", ingr)
    print("join:",",".join(ingr))

    lines = """\
    Java Programing
    Python Programing
    Linux Programing
    """
    print("lines:", lines.split("\n"))
    print("lines:", lines.strip().splitlines())


if __name__ == '__main__':

    #define_str()
    #str_oper()
    #search_methods()
    #modify_and_replace()
    split_join_methods()
