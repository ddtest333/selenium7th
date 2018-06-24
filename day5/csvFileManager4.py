#导包
import  csv

import os


class  CsvFileManager4:
    def read(self, filename):
        list =[]   #声明一个空列表
        #指定csv文件的路径
        #path ="C:\Users\51Testing\PycharmProjects\selenium7th\data\test_data.csv"
        #这样生产的path路径有个缺点?可移值性比较差
        #更好的方法是:
        #os.path.dirname(__file__)这是一个固定的写法,用来获取当前文件的目录
        #os:操作系统 path:路径 driname :目录名 __file__是python内置的变量,表示当前文件路径:C:\Users\51Testing\PycharmProjects\selenium7th\day5
        base_path = os.path.dirname(__file__)
        print(base_path)
#用bast_path的好处:不管项目放到任何路径下面,都可以找到文件的绝对路径
#我们真正想要的是csv文件路径,不是代码文件路径
#所以我们可以通过basepath 计算出csv文件路径
        path = base_path.replace('day5','data/'+ filename)
        print(path)
        #打开指定文件
        #file = open(path,'r')
        #每次打开文件,用完之后都要关闭,释放系统资源
        #上机课用的是try ... finally 的方法
        #更常用的方法:是 with ...as 的语法结构
        with open(path,'r') as  file:
            data_table = csv.reader(file)
            #循环遍历数据表中的每一行
            for row in data_table:
                print(row)


        #5/声明一个二维列表,保存data
                list.append(row)
                #在read 方法末尾.返回这个列表
        return  list

#一个CSV文件只适合保存一组测试用例
#所以不同的测试用例,应该对应不同的csv 文件
#filname 一个变量,可找到该路径下的所有csv 文件, 入需输入 在写入指定的csv文件
if __name__ == '__main__':
    list = CsvFileManager4().read("test_data.csv")
    print(list[0][0])


