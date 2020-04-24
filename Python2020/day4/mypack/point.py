class Point:
    # 클래스 영역:

    instance_count = 0

    # LifeCycle
    def __init__(self,x=0,y=0):
        # 생성자 중복 생성이 안되므로
        # 다양한 형태의 초기화를 지원하는 단 하나의 생성자를 만들어야 한다.
        self.x =x
        self.y =y

        # 생성시 클래스 영역의 instance_count 를 증가
        Point.instance_count +=1

    def __del__(self):  # 소멸자 -> 객체가 삭제될 때
        Point.instance_count -= 1

    def __str__(self):  # print, str -> 문자열 출력 포맷 반한
        return "Point x = {}, y = {}".format(self.x,self.y)

    def __repr__(self): # repr 함수를 호출했을 때 반환하는 문자열
        # 원래 객체를 재현할 수 있어야 한다. -> 개발자용
        return "Point({},{})".format(self.x,self.y)

    def __eq__(self, other):
        #
        if isinstance(other,Point):
            return self.x == other.x and self.y == other.y

    def __add__(self, other):
        if isinstance(other, Point):  # + Point
            return Point(self.x + other.x, self.y + other.y)
        if isinstance(other, int):  # + int
            return Point(self.x + other, self.y + other)
        return self +other

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        if isinstance(other, int):
            return Point(self.x - other, self.y - other)
        return self - other


    # 역이항 연산자
    def __radd__(self, other):  # other + Point

        if isinstance(other, int):  # + int
            return Point(other + self.x ,other + self.y)
        return other + self

    def __rsub__(self, other):  # other - Point

        if isinstance(other, int):  # + int
            return Point(other - self.x ,other - self.y)
        return other - self



    # 인스턴스 메서드
    def set_x(self,x): # 인스턴스 메서드의 첫번째 인자는 반드시 self
        self.x = x # 인스턴스 변수는 self로 명시.

    def get_x(self):
            return self.x


    def set_y(self,y):
        self.y = y

    def get_y(self):
            return self.y


    @classmethod
    def class_method(cls): # cls -> 클래스의 참조 주소
        # cls -> 내부 클래스 영역이 멤버에 접근 가능
        return "인스턴스 카운트:{}".format(cls.instance_count)

    @staticmethod
    def static_method(): # 아무것도 참조할 수 없음.
        print("메서드 수행")