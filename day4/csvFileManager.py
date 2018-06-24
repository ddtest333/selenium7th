#要想读去 csvw  文件 需要导入csv代码库

import csv
#指定文件路径
path='C:\\Users\\51Testing\\PycharmProjects\\selenium7th\\data\\test_data.csv'
#因为字符传中包含反斜杠\t
#每个反斜线前面加一个反斜线
#把每隔反斜线 都改成正斜线
#相比 第二种方法号,
#在字符串中两个反斜线会自动转成一个反斜线
#在window 操作系统中,用反斜线表示目录结构
#但是在linux操作系统中,只有正斜线/ 才能表示目录
#如果用双反斜线,
#在字符串外面加一个字母R ,会认为中间所欲的代码都不存在转义
#print(path)
#3/打开路径所对应的文件
file=open(path,'r')
#4/读取文件的内容,通过什么来读取?CSV
#reader 方法是专门用来读取文件的
data_table =csv.reader(file)
#5/打印内容?循环  for--each语句
#for 是循环的关键字  item 代表 每一行,每循环一次,item 就代表最新的一行数据
#data_table  表示整个文件中的所有数据
for item in  data_table:
    print(item)
#很多的测试用例可能都需要从表中读取数据,所以我们应该对这这些代码做简单那的封装,键一个文件 叫 csvFileManager2 把以上代码封装到一个方法中,并且在建一个文件来读取 封装号的方法

