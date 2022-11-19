from Data.test_objects import CatFactsAsyncAPi
from Utils.base_test_case import BaseTestCase
from Adaptors.sync_adaptors import SyncRequestsAdapter as Request

class TestEndpoints(BaseTestCase):
    def setUp(self):
        super(TestEndpoints, self).setUp()
        self.endpoint_url = CatFactsAsyncAPi.get_randomCatFact().endpoint

    def tearDown(self):
        super(TestEndpoints, self).tearDown()


    def test_cat_facts(self):

        func = Request.get_request(self.endpoint_url)

        assert func.status_code == 200