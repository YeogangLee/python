import pymysql

class MydaoPrc:
    def __init__(self):
        self.conn = pymysql.connect(
                        user="root", password="python",
                        host="localhost", database="_stock_old")
        self.curs = self.conn.cursor()
        
    def selec_stock_min(self):
        sql = """
        SELECT min(s005180)
          FROM stock_sync_0121        
        """
        self.curs.execute(sql)
        min = self.curs.fetchall()
        
        return min 

    def selec_stock_max(self):
        sql = """
        SELECT max(s005180)
          FROM stock_sync_0121        
        """
        self.curs.execute(sql)
        max = self.curs.fetchall()
        
        return max
        
    def __del__(self):
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    de = MydaoPrc()
    result = de.show_stock()
    print(result)