"""
입력값이 q 면 루프를 탈출한다
입력값이 d, w면 금액을 입력받는다
q, d, w 이외의 값이면 ?를 출력한다
금액을 총액에 합산(d) 혹은 차감(w)한다
"""

Balance = 0 # 잔액
flag =1     # 종료 버튼

while(flag):

    method = input("method:")

    if method == 'd' : # 입금
        Amount = int(input("Amount:"))
        Balance = Balance + Amount
        print("Balance:",Balance)

    elif method == 'w' : # 출금
        Amount = int(input("Amount:"))
        Balance = Balance - Amount
        print("Balance:",Balance)

    elif method == 'q' : # 종료
        print("END")
        flag = 0

    else:
        print("?")



