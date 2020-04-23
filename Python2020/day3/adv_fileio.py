# - 파일 타입: t, b
# - 작업 : r, w, a


def write_txt():
    f =open("./sample/test.txt", "wt", encoding="UTF-8")
    size = f.write("python programing")
    print("written size: {}".format(size))

    f.close()

def read_text():
    f = open("./sample/sangbuk.csv","rt", encoding="UTF-8")
    data = f.read()
    f.close()
    print("data:\n",data)

def read_multiline():
    with open("./sample/sangbuk.csv","rt", encoding="UTF-8") as f:
        while True:
            line = f.readline()
            # 체크
            if not line: # 읽어온 데이터가 빈 라인이면..
                break
            print(line)

def read_multiline2():
    with open("./sample/sangbuk.csv", "rt", encoding="UTF-8") as f:
        lines = f.readlines()


    # print(lines)
    for index, line in enumerate(lines):
        print("{}번째 선수: {}".format(index+1,line))

def convert_csv_to_list():
    players = []

    with open("./sample/sangbuk.csv", "rt", encoding="UTF-8") as f:
        while True:
            line = f.readline()
            if not line:
                break
            info = line.strip().split(",")
            info = [word.strip() for word in info ]


            player = {
                "name" : info[0],
                "backno" : int(info[1]),
                "height" : float(info[2]),
                "position" : info[3]
            }

            players.append(player)

    return players

import  pickle
def serialize_ex():
    players = convert_csv_to_list()
    # 기본적으로 피클은 단일 객체 직력화를 위한 모듈
    with open("./sample/players.bin", "wb") as f:
        for player in players:
            pickle.dump(player,f)

def deserialize_ex():

    # 역 직렬화
    players =[]
    with open("./sample/players.bin", "rb") as f:
        while True:
            # 예외 처리

            try:

                player = pickle.load(f)
                players.append(player)

            except EOFError:
                break

    print("복원된 개체:", players)




if __name__ == '__main__':
    # write_txt()
    # read_text()
    # read_multiline2()
    # convert_csv_to_list()
    # serialize_ex()
    print(convert_csv_to_list())