
str = "Life is too short, You need Python"

#이 문자열 내의 글자를 모두 소문자로 변경합니다.
#이 문자열 내의 공백과 ,를 제거합니다.
#이 문자열을 list로 형변환한 후 lst 변수에 담아 봅니다.
lst = "Life is too short, You need Python".replace(",","").lower().split()
print(str)
print(lst)

#lst를 set로 형변환하여 chars 변수에 담아 봅시다.
#chars를 화면에 출력해 봅시다.
chars = set(lst)
print(chars)


#chars를 다시 list로 형변환하여 lst에 담아 봅시다.
#lst를 알파벳 순으로 정렬하고, 길이를 출력해 봅시다.
lst=list(chars)
print(sorted(lst),len(lst))


