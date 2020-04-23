"""
- datetime 객체 : 년월일시분초마이크로초, 요일
- date 객체 : 년월일, 요일
- time 객체 : 시분초마이크로초
- timedelta 객체 : 두 타임간의 간격 정보 일수, 초, 마이크로초
"""
import datetime
def get_datetime():
    now = datetime.datetime.now()
    print("현재 :", now )
    print("속성들 :", now.year, now.month, now.day,
          now.hour,now.minute,now.second,now.microsecond)
    print("요일 : ", now.weekday())

    # 생성자 이용 : 최소 년월일 정보는 부여해야 한다.
    past = datetime.datetime(1999,12,31)
    print("과거:",past)

    # 날짜 객체 반환 : date() 메서드
    now_date = now.date()
    print("오늘 날짜:", now_date)
    print("date의 속성과 메서드:", now_date,now_date.month,now_date.weekday())

    # 시간객체 반환 : time() 메서드
    now_time = now.time()
    print("현재 시간:", now_time)
    print("time의 속성과 메서드 :", now_time.hour,now_time.minute,now_time.second,now_time.microsecond)


def timedelta_ex():
    # 두 개의 datetime 객체는 대소를 비교할 수 있다.
    now = datetime.datetime.now()
    past = datetime.datetime(1996, 1, 21)

    print("now 가 past보다 미래인가?", now > past)

    #
    diff = now - past
    print("흘러간 시간:",diff,type(diff))
    print("{}부터 {} 까지 총 {} 초가 지났다.".format(past,now,diff.total_seconds()))

    #
    # 오늘부터 백일 후
    delta = datetime.timedelta(days=100, seconds=0, microseconds=0)
    print(delta)
    print(now + delta)
    print((now+delta).weekday())


def format_date():
    # datetime -> str : .strftime
    # str -> datetime : .strptime
    now = datetime.datetime.now()
    print(now)
    print("strftime:", now.strftime("%Y년%m월%d일%H시%M분%S초"))

    s= "1996년 1월 21일 12시 30분"
    print("strptime:",datetime.datetime.strptime(s,"%Y년 %m월 %d일 %H시 %M분"))




if __name__ == '__main__':
    # get_datetime()
    # timedelta_ex()
    format_date()




