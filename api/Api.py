"""
============================
@auther:多测师-黄sir
@time:2021/5/20:15:17
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
'''此模块用来封装所有接口访问方法'''
# 以下3行代码用来调试数据使用
# import requests,unittest
# from config.Config import *
# session = requests.Session()
class Cms_Api:
    '''单例模式的写法'''
    @classmethod
    def set_session(cls,session):
        cls.session = session
    @classmethod
    def get_session(cls):
        return cls.session
    # 封装接口访问的方法

    def test_cms(self,cms_api):
        type = [['post','put','patch'],['delete','head','get','options']]
        if cms_api[0] in type[0]:
            self.response = self.session.request(method=cms_api[0],url=cms_api[1],data=cms_api[2],headers=cms_api[3])
        elif cms_api[0] in type[1]:
            self.response = self.session.request(method=cms_api[0],url=cms_api[1],params=cms_api[2],headers=cms_api[3])
        # print(self.response)
        return self.response
if __name__ == '__main__':
    c = Cms_Api()
    c.set_session(session)
    c.get_session()
    api = ('post',login_url,login_data,login_headers)
    Cms_Api().test_cms(api)




