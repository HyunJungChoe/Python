import  sqlite3

class Database:
    # Lifecycle
    def __init__(self, db=None):
        self.conn = None
        self.cursor = None
        if db: # 디비 정보가 전달 되면
            self.open(db)

    def __enter__(self): # with ~ as 로 시작할 때 호출
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()



    # 인스턴스 메서드
    def open(self,db):
        try:
            self.conn = sqlite3.connect(db)
            self.cursor=self.conn.cursor()
        except sqlite3.Error as e:
            print("접속 에러")

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def execute_select(self, sql, params = None):
        if not params: # 파라미터가 전달되지 않음
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

        return self.cursor.fetchall()

    def execute_cud(self, sql, params = None):
        if not params:  # 파라미터가 전달되지 않음
            self.cursor.execute(sql, params)
        else:
            self.cursor.execute(sql)

        return self.cursor.rowcount







