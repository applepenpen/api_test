import pymssql
import os
import configparser as CP
from pymssql import OperationalError
from config import host,port,user,password,db_name,charset


class DB:
    def __init__(self):
        try:
            self.conn=connect(
                host=host,
                port=int(port),
                user=user,
                password=password,
                db=db_name,
                charset=charset
            )
        except OperationalError as e:
            print('SQl server error %d:%s'%(e.args[0],e.args[1]))
        else:
            self.cursor=self.conn.cursor()

    def execute_sql(self,command,sql):
        # 如果为查询指令
        if command in('select','SELECT'):
            sql=sql.encoder('utf-8')
            try:
                self.cursor.execute(sql)
                result=self.cursor.fetchall()
                return result
            except Exception as e:
                print(e)
            finally:
                self.conn.close()
        elif command in('delete', 'DELETE', 'update', 'UPDATE', 'insert', 'INSERT'):
            #如果为删改查
            sql = sql.encoder('utf-8')
            try:
                self.cursor.execute(sql)
                self.conn.commit()
            except Exception as e:
                self.conn.rollback()
                print(e)
            finally:
                self.conn.close()
        else:
            print('Command Error!')


if __name__ == '__main__':

    # sel_sql = cf.get('SQL', 'SELECT')
    # s = DB().execute_sql('select', sel_sql)
    print(DB().execute_sql('select', cf.get('SQL', 'SELECT'))[0][0])



