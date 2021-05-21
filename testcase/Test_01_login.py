"""
============================
@auther:多测师-黄sir
@time:2021/5/20:16:19
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
import unittest,requests
from api.Api import Cms_Api
from config.Config import *
class Login(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        Cms_Api().set_session(cls.session)
        Cms_Api().get_session()

    def test_01(self):
        cms_api = ('post',login_url,login_data,login_headers)
        self.response = Cms_Api().test_cms(cms_api)
        # print(self.response.text)
        assert self.response.json()['msg'] == '登录成功！'


if __name__ == '__main__':
    unittest.main()