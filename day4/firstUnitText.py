#第一个单元测试框架的实力
#1/要想用unittest框架 首先要导包
#为什么selenium 需要先安装或者解压?unitest不需要
#因为unitext 比 selenium 更常用,几乎所有测试都要用unittest
#所以 python 把 unittest 继承在python SDK 中了,不需要单独下载 只要安装 python 就有
import  unittest

#2 创建一个类,用来编写自动化测试用例,
# 这个自动化测试用例的类需要继承unittest 框架中的TextCase类
#我们继承了TestCase这个类 ,就说明我们这个类是一个测试用例类
#python 中的类名最好和文件名不一样,文件名首字母小写类名首字母大写
#类名和文件不强制要求,知识一个习惯python
#()表示继承,继承是子类完全继承父类的所有方法和属性,并且有自己扩展的内容
class FirstUnittestTest(unittest.TestCase):
#   3/重写父类的setUp 和 tearDown 方法
    def setUp(self):
#   setUp() 是在测试用例方法执行之前要做的操作
#    类似手工测试中的预置条件
        print(1)
    def tearDown(self):
#        tearDown()是在测试用例方法执行之后要做的操作,比如可能需要还原测试场景,清除脏数据
        print(2)#前面要有8个空格
    def test_login(self):
#       这个方法用来执行测试步骤
#     框架规定测试用例方法必须以test开头
        print(3)
    def switch_window(self):
#        窗口切换方法值是希望被调用才能执行
#       只有以test开头的方法才会被当做测试用例,直接执行
        print(4)
    def test_zhuce(self):
        #在python 中类里面的每个方法,都有一个默认参数,叫 self
        #self类似与java  中的this 关键字 代表类本身
        #如果你向用类的属性和方法m,那么必须在前面加self关键字
        #根据光标所在的位置,决定执行什么测试用例
        #光标在哪个方法中,那么就只会运行哪个测试用例
        #贯标在unittest.main() 就会执行所有用例
        self.switch_window()
    #也可以选择重写 setUpClass  和tearDownClass方法
    @classmethod
    def setUpClass(cls):
        print(5)
    @classmethod
    def tearDownClass(cls):
        print(6)
    #写完之后 在unittest.main()位置执行
    #检查setupclass 和setup方法有什么不同
    #classmethod 只在类中所有方法前或者方法后执行一次


#if __name__ == '__main__':这是一个固定的写法
#在程序运行时,通过这句话,可以自动判断当前文件是不是程序的入口
#如果当前文件是程序的入口,那么就会执行if 子句中的内容

if __name__ == '__main__':
 #unittest.main () 可以理解为当前文件的主函数,会自动调用类中的的左右测试用例方法
    unittest.main()





