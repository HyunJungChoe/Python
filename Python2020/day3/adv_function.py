# 글로벌 객체
x = 1

def func1(a):
    print("func1:",locals())
    return a + x


def func2(a):
    x = 2
    print("func2:", locals())
    return a + x

def func3(a):
    global x # 여기부터 진행되는 x는 글로벌 변수임을 명시

    x = 3
    print("func3:", locals())
    return a + x
    # 가급적 함수 내부에서 글로벌 객체를 다루지는 말자 -> 권장


def sum(a,b):
    return a+b

def incr(a,step=1):
    return a+step
    # 인자는 전달되지 않으면 기본값 1을 사용

def get_total(*args):
    # print(("args:",args))

    total =0
    for num in args:
        if isinstance(num,(int,float)):
            total += num

    # 리스트 내포
    # total = sum([ num for num in args if isinstance(num,(int, float))])

    return total

def test_kwd_arg(a, b, *args, **kwd):
    print("고정 인수:", a,b)
    print("가변 인수:", args)
    print("사전 인수:", kwd)
    #순서가 중요! 고정인수, 가변인수, 사ㅏ전인수 순으로 선언

# callback
# 함수는 객체다 -> 다른 변수에 할당될 수 있다.

def calc(a,b,func):   # func는 함수
    if callable(func): # -> 함수임을 확인
        return func(a,b) # Callback

def sort_by_lambda():
    lst = [80,92,73,99,86,42]
    # 기본적인 소트
    print("SORT ASC:", sorted(lst))
    # 10으로 나눈 나머지의 역순 정렬
    print("Custom sort DESC:", sorted(lst, reverse=True, key=lambda x:x % 10))


def handling_exception():
    lst = []


    try:
        lst[0] = 1
        num = int("123")
    # 주의 : 구체적 예외를 앞쪽에서 점검
    # 가장 마지막에 모든 예외 처리용 Exception 을 배치
    except IndexError as e:
        print("인덱스 오류 :",e,type(e))
    except ValueError as e:
        print("컨버팅 오류:", e, type(e))
    except Exception as e:
        print("예외:", e, type(e))
    else:  # try 블록에서 예외 없이 잘 처리 되었을 때
        print("예외 없음 !")
    finally: # 예외 유무 상관 없이 가장 마지막에 수행
        print("~~~")

    # 예외 있을 때: try -> except -> finally
    # 예외 없을 때: try -> else -> finally
    print("finish")

def raise_exception():
    def beware_dog(animal):
        # animal 이 dog 예외 던지기
        if animal.lower()=="dog":
            # 호출하는 함수에게 예외 처리를 위임
            raise RuntimeError("강아지는 출입 안됩니다.")
        else:
            print("어서오세요 {}".format(animal))

    try:
        beware_dog("cow")
        beware_dog("cat")
        beware_dog("dog")
    except Exception as e:
        print("예외:",e)



if __name__ == '__main__':

    # print("func1:",func1(10))
    # print("global x:", x)
    #
    #
    # print("func2:", func2(10))
    # print("global x:", x)
    #
    # print("func3:", func3(10))
    # print("global x:", x)
    # print("7+3",sum(10,20))
    # print("incr(10):", incr(10,2))
    # print("incr(10)", incr(10))
    # print("키워드 인수",incr(step=3,a=20)) # 함수 선언부에 정의한 인수의 이름으로 값을 전달
    #
    # print("get_total:",get_total(1,2,3))
    # print("get_total:", get_total(1, 2, 3,4,5))
    # print("get_total:", get_total(1, 2, "3",4,5))

    # test_kwd_arg(10,20,30,40,"python", opt1= 10, opt2="python")
    #
    # print("calc <- sum:",calc(10,20,sum))
    # print("calc <- lambda:",calc(10,20,lambda a,b: a-b))

    # sort_by_lambda()

    # handling_exception()
    raise_exception()