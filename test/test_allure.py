class Test_allure:


    def setup(self):
        assert 0

    def teardown(self):
        assert 1
    @allure.step('我是测试步骤001')
    def test_al(self):
        assert 1
