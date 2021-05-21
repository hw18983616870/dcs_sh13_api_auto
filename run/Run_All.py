"""
============================
@auther:多测师-黄sir
@time:2021/5/20:16:34
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
'''此模块用来执行所有的测试用例'''
import unittest
from utils.HTMLTestRunner3_New import HTMLTestRunner
from utils.mail3 import SendMail
from time import strftime
def run_all():
    path =  r'D:\workspace\dcs_sh13_api_auto\testcase'
    report_path = r'D:\workspace\dcs_sh13_api_auto\report'
    discover = unittest.defaultTestLoader.discover(start_dir=path,pattern='Test*.py')
    now = strftime('%Y-%m-%d-%H-%M-%S')
    filename = report_path+'\\'+str(now)+'_CMS_API_AUTO_report.html'
    f = open(file=filename,mode='wb')
    runner = HTMLTestRunner(
        stream=f,
        title='CMS平台接口自动化测试用例',
        description='用例执行情况如下：',
        tester='dcs_sh13'
    )
    runner.run(discover)
    f.close()
    sendmail = SendMail(send_msg=filename,attachment=filename)
    sendmail.send_mail()
run_all()