



def reverse_sort():
    lst = [80,90,85, 75, 100, 60, 90 ]
    print("원본:",lst)
    print("반전:", lst[::-1]) # 순서가 역순인 새 리스트
    lst.reverse()
    print("원본:",lst)

    # 정렬
    # 함수로서의 sorted -> 새 리스트를 반환
    # 메서드로서의 sort -> 내부 데이터를 변경
    print("sort asc:", sorted(lst)) # 오름차순
    print("sort desc:", sorted(lst,reverse=True)) # 내림차순

    # 정렬기준의 변경 : key 함수 정의
    print("sort desc key=str:", sorted(lst, key=str, reverse=True ))

    lst2 =[ 19,46,37,20,91,53,77]

    def key_func(x):
        return x % 2

    print("custom sort desc key= key_func:", sorted(lst2, key=key_func, reverse=True))

def stack_ex():
    #후입 선출(LIFO)

    stack =[]
    stack.append(10)
    stack.append(20)
    stack.append(30)
    print("Stack:", stack )

    #output
    print("pop:", stack.pop())
    print("pop:", stack.pop())
    print("pop:", stack.pop())
    print('stack:', stack)

    if len(stack):
        print("pop:", stack.pop())
    else:
        print("Empty")


def queue_ex():
    queue =[]
    queue.append(10)
    queue.append(20)
    queue.append(30)
    print('queue:', queue)
    print("pop:", queue.pop(0))
    print("pop:", queue.pop(0))
    print("pop:", queue.pop(0))

    if len(queue):
        print("pop:", queue.pop(0))
    else:
        print("Empty")

def loop():
    words= "Life is too short, you need python".replace(",","").upper().split()
    print(words)





if __name__ == '__main__':
    #reverse_sort()
    #stack_ex()
    #queue_ex()
    loop()
