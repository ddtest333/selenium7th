import  csv
#每个测试用例对应这不同的csv 文件
#每条测试用例都会打开一个csv文件
class CsvFileManager3:
    @classmethod
    def read(self) -> object:
        path ='/Users/51Testing/PycharmProjects/selenium7th/data/test_data.csv'
        file = open(path, 'r')
        try:#try尝试执行以下代码

            data_table =csv.reader(file)

            for item in data_table:
                print(item)
            #方法最后应该添加一个close 方法
        finally:

            file.close()
            print("123123")
if __name__ == '__main__':
    csvr=CsvFileManager3()
    csvr.read()
