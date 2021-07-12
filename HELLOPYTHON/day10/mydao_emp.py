import pymysql

class DaoEmp:
    def __init__(self):
        self.conn = pymysql.connect(
                        user="root", password="python",
                        host="localhost", database="mypydb")
        self.curs = self.conn.cursor()
        
    def letsgo(self):
        return 'g2'
        
    def insert(self,e_id,e_name,tel,address):
        sql = f"""
        insert into emp 
            (e_name,tel,address,in_user_id,in_date,up_user_id,up_date) 
        values 
            ('{e_name}','{tel}','{address}','1',DATE_FORMAT(NOW(), '%Y%m%d.%H%m%s'),'1',DATE_FORMAT(NOW(), '%Y%m%d.%H%m%s'))
        """
        
        self.curs.execute(sql)
        self.conn.commit()
        cnt = self.curs.rowcount
        return cnt
    
        
    def selectlist(self):
        ret = []
        sql = """
        SELECT
            e_id,
            e_name,
            tel,
            address,
            in_user_id,
            in_date,
            up_user_id,
            up_date
        FROM emp
        """ 
        self.curs.execute(sql)
        rows = self.curs.fetchall()
        for row in rows:
            ret.append({'e_id':row[0],'e_name':row[1],'tel':row[2],'address':row[3],'in_user_id':row[4],'in_date':row[5],'up_user_id':row[6],'up_date':row[7]})        
        
        return ret
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
    
    
if __name__ == '__main__':
    de = DaoEmp()
    arr = de.selectlist()
    print(arr)
