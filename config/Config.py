"""
============================
@auther:多测师-黄sir
@time:2021/5/20:14:59
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
'''此模块用于存放所有接口的配置信息'''
#登录接口
login_url = 'http://192.168.6.136:8082/cms/manage/loginJump.do'
login_data = {
        'userAccount':'admin',
        'loginPwd':'123456'
        }
login_headers = {'Content-Type':'application/x-www-form-urlencoded'}
#用户查询接口
queryUserList_url = 'http://192.168.6.136:8082/cms/manage/queryUserList.do'
queryUserList_data = {
            'startCreateDate': '',
            'endCreateDate':'',
            'searchValue': '',
            'page': 1
        }
queryUserList_headers = {'Content-Type': 'application/x-www-form-urlencoded'}
