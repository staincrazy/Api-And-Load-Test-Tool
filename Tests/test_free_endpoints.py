from Data.test_objects import CatFactsAsyncAPi
from Utils.base_test_case import BaseTestCase
from Adaptors.async_adaptors import AsyncRequestsAdapter as asyncRequest
from Adaptors.sync_adaptors import SyncRequestsAdapter as syncRequest


class TestEndpoints(BaseTestCase):
    def setUp(self):
        super(TestEndpoints, self).setUp()
        self.endpoint_url = CatFactsAsyncAPi.get_randomCatFact().endpoint

    def tearDown(self):
        super(TestEndpoints, self).tearDown()

    def test__get_cat_facts_response_200(self):
        func = syncRequest.get_request(self.endpoint_url)

        assert func.status_code == 200

        print(func.json())

    def test__async_get_cat_facts__response_200(self):
        func = asyncRequest.get_multiple_requests(self.endpoint_url)

        for i in range(len(func)):

            print(func[i].json())

        assert any(func[i].status_code == 200 for i in range(len(func)))
