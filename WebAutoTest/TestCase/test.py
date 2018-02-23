import pytest, allure

def pytest_configure(config):
    allure.environment(report='Allure report', browser='Chrome 63')

class Test_a():
    # @pytest.fixture('module', autouse=True)
    def setup_method(self, method):
        self.a = 'a'
        print('setup')

    @allure.feature('Feature1')
    @allure.story('Story1')
    def test_a(self):
        with pytest.allure.step('打印a'):
            print(self.a)
        with pytest.allure.step('结束'):
            pass

    @allure.feature('Feature1')
    @allure.story('Story2')
    def test_b(self):
        print(self.a+'------------')

    @allure.feature('Feature2')
    @allure.story('Story1')
    def test_c(self):
        print(self.a + '------------')

    @staticmethod
    def teardown_method(method):
        f = open('../testresult/screenshot/test_address_1.png', 'rb').read()
        allure.attach('IMG', f, allure.attach_type.PNG)
        print('teardown')