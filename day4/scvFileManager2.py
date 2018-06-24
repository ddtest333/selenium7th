import  csv

class CsvFileManager2:
    @classmethod
    def read(self) -> object:
        path ='/Users/51Testing/PycharmProjects/selenium7th/data/test_data.csv'
        file =open(path,'r')
        #通过csv 代码库读取打开额csv 文件,获取文件中数据
        data_table =csv.reader(file)

        for item in data_table:
            print(item)
#如果想测试一下
if __name__ == '__main__':
    csvr=CsvFileManager2()
    csvr.read()
