import sqlite3
import pandas as pd

class checkAnsQuery:
    def __init__(self, test_query, ans_query, db_connection):
        self._test_query = test_query
        self._ans_query = ans_query
        self._db_connection = db_connection
        test = pd.read_sql(self._test_query, self._db_connection)
        self._test = test
    def check_syntax(self):
        try:
            ans = pd.read_sql(self._ans_query, self._db_connection)
            self._ans = ans
        except Exception as e:
            print("查詢語法有誤，錯誤訊息為：\n")
            print(str(e))
    def check_frame(self):
        if hasattr(self, '_ans'):
            try:
                pd.testing.assert_frame_equal(self._test, self._ans)
                print("測資比對正確！")
            except AssertionError as e:
                print("測資比對有誤，錯誤訊息為：\n")
                print(str(e))
        else:
            pass
    def run_test(self):
        self.check_syntax()
        self.check_frame()