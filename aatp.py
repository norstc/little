# Automated Acceptance Test Platform
# Date: 2020.11.4
# Author: Zhangjh

# -*- coding: utf-8 -*-
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url_euop_175 = "http://192.168.1.175:8099"
        self.base_url_euop_181 = "http://192.168.1.181:8080"
        self.username="zhangjh@sh-stt.com"
        self.phone="15800407048"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url_euop_175+"/euop/user/tologin.do")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys(self.phone)
        driver.find_element_by_id("imgCode2").click()
        driver.find_element_by_id("imageValidCode2").click()
        driver.find_element_by_id("imageValidCode2").clear()
        driver.find_element_by_id("imageValidCode2").send_keys("1")
        driver.find_element_by_id("ssoLogin").click()

    def test_login_to_person(self):
        driver = self.driver
        driver.get("http://192.168.1.175:8099/euop/user/login.do")
        driver.find_element_by_id("username").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(self.username)
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys(self.phone)
        driver.find_element_by_id("imageValidCode2").clear()
        driver.find_element_by_id("imageValidCode2").send_keys("1234")
        driver.find_element_by_id("ssoLogin").click()
        # 处理警告弹窗，可以先用time.sleep 判断是否因为没有等到弹窗而报错
        # time.sleep(6)
        # 弹窗处理
        try:
            WebDriverWait(driver, 3).until(EC.alert_is_present(),
                                           "Timed out waiting for PA creation confirmation popup to appear")
            alert = driver.switch_to.alert
            self.assertEqual(u"短信发送成功，请接收", alert.text)
            alert.accept()
            print("alert accepted")
        except TimeoutException:
            print('no alert')
        driver.find_element_by_id("txtMobileSn").click()
        driver.find_element_by_id("txtMobileSn").clear()
        driver.find_element_by_id("txtMobileSn").send_keys("1")
        driver.find_element_by_id("btnVaild").click()
        try:
            self.assertEqual(u"中国移动集团门户网站运营管理平台", driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"发布管理").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    # run all tests
    # unittest.main()
    # run single test
    # from command line: python test_euop_startpage.py Login.test_login_to_person
    # from program inside
    suite = unittest.TestSuite()
    suite.addTest(Login("test_login_to_person"))
    runner = unittest.TextTestRunner()
    runner.run(suite)


