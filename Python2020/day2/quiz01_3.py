


students = [
    {
        "name": "Kim",
        "kor": 80,
        "eng": 90,
        "math": 80
    },
    {
        "name": "Lee",
        "kor": 90,
        "eng": 85,
        "math": 85
    }
]

# 각 리스트를 딕셔너리로 변환
dic1=dict(students[0])
dic2=dict(students[1])

#두 학생의 kor, eng, math 합계 점수와 평균을 사전 데이터에 "total", "average" 키값으로 넣어 봅시다.
dic1["total"]= dic1["kor"] +dic1["eng"] + dic1["math"]
dic1["average"]= dic1["total"] /3
dic2["total"]=dic2["kor"] +dic2["eng"] + dic2["math"]
dic2["average"]= dic2["total"] /3

print(dic1)
print(dic2)


