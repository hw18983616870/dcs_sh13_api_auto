"""
============================
@auther:多测师-黄sir
@time:2021/5/20:16:30
@email:hw18983616870@163.com
@website:www.duoceshi.cn
============================
"""
from api.Api import Cms_Api
from config.Config import *
import unittest
class QueryUserList(unittest.TestCase):
    def test_01(self):
        self.cms_api = ('post',queryUserList_url,queryUserList_data,queryUserList_headers)
        self.response = Cms_Api().test_cms(self.cms_api)
        assert self.response.json()['msg'] == '查询用户成功！'
