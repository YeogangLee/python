import pymysql

class MystockDao:
    
    def __init__(self):
        self.conn = pymysql.connect(user="root", password="python",
                               host="localhost", database="_stock_old")
        self.curs = self.conn.cursor()
    
    def get_first_day_count(self):
        ret = []
        sql = """
        SELECT count(s005180)
          FROM stock_sync_0121
         WHERE '20201215.0000' < in_time AND '20201215.2359' > in_time
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append(row[0])

        return ret
        
    def get_first_day_list(self):
        ret = []
        sql = """
        SELECT s005180
          FROM stock_sync_0121
         WHERE '20201215.0000' < in_time AND '20201215.2359' > in_time
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append(row[0])

        return ret
    
    def get_last_day_count(self):
        ret = []
        sql = """
         SELECT count(s005180)
           FROM stock_sync_0121
          WHERE '20210121.0000' < in_time AND '20210121.2359' > in_time
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append(row[0])

        return ret
        
    def get_last_day_list(self):
        ret = []
        sql = """
        SELECT s005180
          FROM stock_sync_0121
         WHERE '20210121.0000' < in_time AND '20210121.2359' > in_time
        """
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append(row[0])

        return ret
    
    #
    
    def get_prices(self, c_name):
        ret = []
        sql = f"""select s_code, c_name, price, crw_date from stock where c_name='{c_name}'"""
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        # print(rows) 
        for row in rows:
            ret.append(row[2])
            
        return ret
    
    def get_all_names(self):
        ret = []
        sql = f"""select c_name from stock group by c_name"""
        
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        # print(rows) 
        for row in rows:
            ret.append(row[0])
            
        return ret
        
        
    
    def retrieveAll(self):
        ret = []
        sql = f""" SELECT s_code, c_name from stock GROUP BY s_code, c_name"""
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for idx, row in enumerate(rows):
            ret.append(row[1])
            
        return ret
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
        
        
if __name__ == '__main__':
    # ds = DaoStock()
    # ds.get_prices("삼성전자")
    
    md = MystockDao()
    result = md.get_day_list()
    count = md.get_day_count()
    print(count)
    