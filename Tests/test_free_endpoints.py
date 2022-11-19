from Utils.base_test_case import BaseTestCase


class TestEndpoints(BaseTestCase):
    def setUp(self):
        super(TestEndpoints, self).setUp()
        self.endpoint_url = ""

    def tearDown(self):
        super(TestEndpoints, self).tearDown()


    def test_cat_facts(self):
        pass