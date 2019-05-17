#  coding utf-8
# @time      :2019/4/2316:39
# @Author    :zjunbin
# @Email     :648060307@qq.com
# @File      :TestLogin.py
from selenium import webdriver
from PageObject.login_page import LoginPage
from PageObject.index_page import IndexPage
from Testdatas import login_datas as ld
from ddt import ddt,data
import unittest
import pytest


@pytest.mark.usefixtures("prepara_env")
@pytest.mark.login
class TestLogin:

    @pytest.mark.smoke  #打一个标签  @pytest.mark.标签名
    def test_login_success(self,prepara_env):
        LoginPage(prepara_env).Login(ld.success_data['username'],ld.success_data['pwd'],ld.success_data['code'])
        print(IndexPage(prepara_env).isExist_quitEle())
        assert(IndexPage(prepara_env).isExist_quitEle())

    @pytest.mark.parametrize("item",ld.datacase) #pytest参数化测试数据
    def test_login_null_error(self,item, prepara_env):
        print(item['username'])
        LoginPage(prepara_env).Login(item['username'],item['pwd'],item['code'])
        assert item['excepted'] == LoginPage(prepara_env).get_find_from_loginArea()


    @pytest.mark.parametrize("item",ld.dataerror)
    def test_login_error(self, item ,prepara_env):
        LoginPage(prepara_env).Login(item['username'], item['pwd'], item['code'])
        assert item['excepted'] == LoginPage(prepara_env).get_error()


