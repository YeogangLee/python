import mariadb 

class DaoStock:
    
    def __init__(self):
        self.conn = mariadb.connect(user="root", password="python",
                               host="localhost", database="mypydb")
        self.curs = self.conn.cursor() 
    
    def get_prices(self, c_name):
        ret = []
        sql = f"""select s_code, c_name, price, crw_date from stock where c_name='{c_name}'"""
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        # print(rows) 
        for row in rows:
            ret.append(row[2])
            
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
    
    ds = DaoStock()
    # list_prices = ds.get_prices("삼성전자")
    # print(list_prices)
    list_retrieve = ds.retrieveAll()
    print(list_retrieve)
    
    