import  re

def using_regex():
    # 방법1. 패턴 컴파일 후 이용
    source = "Life is too short, You need Python"
    p = re.compile(r"p[a-z]+") # 첫 글자가 p고 a-z가 한글자 이상
    # print(p.match(source))
    p = re.compile(r"L[a-z]+") # 첫 글자가 L고 a-z가 한글자 이상

    match = p.match(source)
    print(match)
    print("matching result:", match.group())

    # 방법2. 축약 -> 컴파일과 매칭을 동시에
    print(re.search("L[a-z]+",source))
    print(re.search("P[a-z]+",source))







if __name__ == '__main__':
    using_regex()