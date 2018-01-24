import sys
sys.path.append('../Page')
import unittest
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from Page_Base import Page
from Page_Home import Home
from Page_UserInvoice import UserInvoice

class TestUserInvoice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.page = Page(self.driver)
        self.environment = self.page.config_reader('environment.conf', 'Environment', 'environment')
        if self.environment == 'staging':
            self.driver.get('http://ps.ehsy.com')
        else:
            self.driver.get('http://new.ehsy.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.home = Home(self.driver)
        self.user_invoice = UserInvoice(self.driver)

    def test_invoice_personal(self):
        loginname = self.page.config_reader('test_order.conf', '个人地址发票账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '个人地址发票账号', 'password')
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.user_invoice.wait_click(self.user_invoice.my_invoice)
        # 公司类型的发票
        self.user_invoice.add_company_invoice()
        self.user_invoice.edit_company_invoice()
        self.user_invoice.company_change_personal()
        self.user_invoice.set_default_invoice()
        self.user_invoice.delete_invoice()
        # 个人类型发票
        self.user_invoice.add_personal_invoice()
        self.user_invoice.edit_personal_invoice()
        self.user_invoice.personal_change_company()
        self.user_invoice.set_default_invoice()
        self.user_invoice.delete_invoice()
        # 增值税发票
        self.user_invoice.add_receipt_invoice()
        self.user_invoice.edit_receipt_invoice()
        self.user_invoice.set_default_receipt_invoice()
        self.user_invoice.delete_invoice()

    def test_invoice_company_distribution(self):
        loginname = self.page.config_reader('test_order.conf', '分销地址发票账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '分销地址发票账号', 'password')
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.user_invoice.wait_click(self.user_invoice.my_invoice)
        # 公司类型的发票
        self.user_invoice.add_company_invoice()
        self.user_invoice.edit_company_invoice()
        self.user_invoice.company_change_personal()
        self.user_invoice.set_default_invoice()
        self.user_invoice.delete_invoice()
        # 个人类型发票
        self.user_invoice.add_personal_invoice()
        self.user_invoice.edit_personal_invoice()
        self.user_invoice.personal_change_company()
        self.user_invoice.set_default_invoice()
        self.user_invoice.delete_invoice()
        # 增值税发票
        self.user_invoice.add_receipt_invoice()
        self.user_invoice.edit_receipt_invoice()
        self.user_invoice.set_default_receipt_invoice()
        self.user_invoice.delete_invoice()

    def test_invoice_company_terminal(self):
        loginname = self.page.config_reader('test_order.conf', '终端地址发票账号', 'login_name')
        password = self.page.config_reader('test_order.conf', '终端地址发票账号', 'password')
        self.home.login(loginname, password)
        self.home.go_user_center()
        self.user_invoice.wait_click(self.user_invoice.my_invoice)
        # 公司类型的发票
        self.user_invoice.add_company_invoice()
        self.user_invoice.edit_company_invoice()
        self.user_invoice.company_change_personal()
        self.user_invoice.set_default_invoice()
        self.user_invoice.delete_invoice()
        # 个人类型发票
        self.user_invoice.add_personal_invoice()
        self.user_invoice.edit_personal_invoice()
        self.user_invoice.personal_change_company()
        self.user_invoice.set_default_invoice()
        self.user_invoice.delete_invoice()
        # 增值税发票
        self.user_invoice.add_receipt_invoice()
        self.user_invoice.edit_receipt_invoice()
        self.user_invoice.set_default_receipt_invoice()
        self.user_invoice.delete_invoice()

    def tearDown(self):
        test_method_name = self._testMethodName
        self.driver.save_screenshot('../TestResult/ScreenShot/%s.png' % test_method_name)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(TestUserInvoice('test_invoice_personal'))
    # file = open('../TestResult/EHSY_AutoTest.html', 'wb')
    # runner = HTMLTestRunner(stream=file, title='用户地址测试报告', description='测试情况')
    # runner.run(suite)
    # file.close()
