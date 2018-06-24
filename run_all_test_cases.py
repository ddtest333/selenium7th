#这个文件是用来批量执行unittest的测试用例的
#该文件是我们这个测试工具的唯一入口
#1/导入unittest, 因为批量执行测试用例的功能由unittest代码库提供的
import smtplib
import  unittest

import os
from email.mime.text import MIMEText

from package.HTMLTestRunner import HTMLTestRunner

def send_mail(path):
    #通过path 打开新生成的测试报告文件
    #html 格式不是文本格式 需要指定以二进制方法打开
    file =open(path,'rb')
    #读取文件的内容,作为邮件正文
    msg = file.read()
    #3.把读取出来的内容转换成MIMETExt的格式
    #电子邮件类型一般分三种:纯文本 plain .html. 富文本
    mime =MIMEText(msg, _subtype='html', _charset="utf-8")
    #4.除了正文以外,还需要设置主题,发件人/收件人/
    mime['Subject']='博为峰自动化测试报告'
    #发件人'bwftest126@126.com', 'abc123asd654'
    #因为发件人需要登录的客服端授权码
    #第三方登录不能直接用密码,必须用授权码
    mime['From']='bwftest126@126.com'
    #收件人写自己的邮箱
    mime['To']=['13661236422@163.com']
    #1/实现SMTP()构造方法
    smtp =smtplib.SMTP()
    #2
    smtp .connect("smtp.126.com")
    #3.
    smtp.login("bwftest126@126.com","abc123asd654")
    smtp.send_message( msg, from_addr='bwftest126@126.com', to_addrs=('13661236422@163.com'))
    smtp.quit()

if __name__ == '__main__':
    #2要想批量执行,首先要明确你要执行哪些测试用例
    #只要西子那个继承了 unnitest.TestCase 的类
    #比如执行这个项目中 所有的 uniitesst 的测试用例
    #defaultTestLoader 是默认的测试用例加载器,可以用来发现所有的测试用例
    #*号表示统配符,可以代替任何字符
    #*Test.py 表示以Test.py 结尾的所有文件
    #.表示当前路径,即项目的跟路径
    #suit 随意起的变量名,suit 本事是测试用例集的意思
    suit = unittest.defaultTestLoader.discover("./day5",pattern='*Test.py')
    #suit = unittest.defaultTestLoader.discover(".", pattern='*.py')#当前项目下的所有测试用例
    #找到测试用例后,执行测试用例
    #TextTestRunner() 本文的测试用例运行器
    #unittest.TextTestRunner().run(suit)
    #4/生成测试报告
    #HTMLTestRunner 类似于TextTestRunner都是批量执行测试用例
    #区别在与,他们执行完所有测试用例的输出
    #一个是Text,另一个是HTML
    #Text 会被打印到控制台中,html 会单独生成一个文件
    #相比于test ,html 结构更清晰
    #所以二者选其一,用HTMLTestRunner代替unittest 原生的测试用例运行器 testtestRunner
    #我们需要把生成的HTML格式的测试报告 保存到一个固定位置方便查看
    #项目根节点下,创建一个文件夹,叫report
    #以后生成的测试报告 就保存到report 下面
    # 5/定义测试报告的保存目录
    base_path =os.path.dirname(__file__)
    path =base_path+"/report/test_report.html"
    #6.创建测试文件
    file = open(path,"wb")
    HTMLTestRunner(stream=file, verbosity=1, title="博为峰测试报告", description='测试环境:Server 2008;浏览器:chrome').run(suit)
    #7/把测试报告作为邮件发送,好处是,可以起到及时提醒的作用
    #前提条件,准备两个邮箱,
    #版本控制的前提条件,申请一个Git账号,并且邮箱激活
    #把HTML格式的测试报告,作为邮件正文发送

