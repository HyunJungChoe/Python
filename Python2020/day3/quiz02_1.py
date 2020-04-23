"""
score1, score2를 입력받아 다음 조건에 부합하면 '합격', 아니면 '불합격'을 출력해 봅시다.
조건 1: 두 과목 모두 50점 이상
조건 2: 두 과목 평균 60점 이상
입력값은 정수라고 가정합니다.


score1 = int(input("점수1 :"))
score2 = int(input("점수2 :"))

if score1 >= 50 and score2 >= 50:
    print("합격")

elif ((score1 + score2)/2) >= 60:
    print("합격")

else:
    print("불합격")

"""

score1 = int(input("점수1? "))
score2 = int(input("점수2? "))
message = "합격" if (score1 >= 50 and score2 >= 50) else "합격" if ((score1 + score2)/2) >= 60 else "불합격"
print("결과:", message)
