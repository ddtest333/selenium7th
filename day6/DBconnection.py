#1.下载并带入代码库:pymysql
import  pymysql


class BDConnection:
    def execute_sql_command(self):
        #2.获取数据库连接
        conn = pymysql.Connect( host ='127.0.0.1', user='root', password="root", database="pirate", port=3306,
                               charset='utf8')
        try:
        #3.获取数据库游标
            cursor = conn.cursor()
            #4.填写sql语句
            #sql ="SELECT * FROM hd_user order by id desc "
        #5.通过游标执行sql语句
            cursor.execute(sql)

        #6.获取执行结果
         # all_result = cursor.fetchall()
        # for row in all_result:
            row = cursor.fetchall()
            #print(row)
            conn.commit()
            return row
        finally:
            conn.close()


if __name__ == '__main__':
    BDConnection().execute_sql_command()



