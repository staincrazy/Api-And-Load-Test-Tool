import random

from Adaptors.async_adaptors import AsyncRequestsAdapter as asyncRequests
from Adaptors.sync_adaptors import SyncRequestsAdapter as syncRequests
from Data.auth_data import getApiKey
from Data.test_objects import ImageApi
from Utils.base_test_case import BaseTestCase


class TestImageApi(BaseTestCase):
    def setUp(self):
        self._api_key = getApiKey()
        self.endpoint_url = ImageApi.get_imageApi().endpoint
        self.webhook_url = 'https://webhook.site/d284e774-acf8-41d9-865f-0e0a9a321afc'

    def test_case_01__correct_creds_and_required_fields__code_200_(self):

        data = {'content_id': str(random.randint(1, 100)),
                'media_url': 'https://cdn.pixabay.com/photo/2020/01/17/18/28/killer-4773702__340.jpg',
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 200
        except AssertionError:
            self.fail('Incorrect code. Check ASAP. Expected 200, got {} instead '.format(resp.status_code))

    def test_case_02__missing_one_required_field__code_400_(self):

        data = {'content_id': None,
                'media_url': 'https://cdn.pixabay.com/photo/2020/01/17/18/28/killer-4773702__340.jpg',
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 400
        except AssertionError:
            self.fail('Incorrect code. Expected 400. Check ASAP. Got {} instead'.format(resp.status_code))

    def test_case_03__missing_both_required_fields_code_400_(self):

        data = {'media_url': '',
                'content_id': '',
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 400
        except AssertionError:
            self.fail('Incorrect code. Expected 400, got {} instead, check ASAP. '.format(resp.status_code))

    def test_case_04__incorrect_data_type__code_400_(self):

        data = {'media_url': None,
                'content_id': 707,
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert resp.status_code == 400
        except AssertionError:
            self.fail('Incorrect code. Expected 400, got {} instead. Check ASAP'.format(resp.status_code))

    def test_case_05__incorrect_credentials__code_401_(self):

        img_url = 'https://9b16f79ca967fd0708d1-2713572fef44aa49ec323e813b06d2d9.ssl.cf2.' \
                  'rackcdn.com/1140x_a10-7_cTC/itfilm-pennywise-it0908-1-1568924719.jpg'

        data = {'media_url': img_url,
                'content_id': str(random.randint(1, 1000)),
                'callback_url': self.webhook_url}

        resp = syncRequests.post_request(endpoint_url=self.endpoint_url, data=data, api_key='18721')

        try:
            assert resp.status_code == 401
        except AssertionError:
            self.fail('Incorrect code. Check ASAP. Expected 401, got {} instead '.format(resp.status_code))

    def test_case_06__multiple_async_post_requests__code_429_(self):

        img_url = "https://i.ytimg.com/vi/Sw5VdceCrLA/maxresdefault.jpg"

        data = {'media_url': img_url,
                'content_id': str(random.randint(1, 1000)),
                'callback_url': self.webhook_url}

        resp = asyncRequests.post_multiple_requests(self.endpoint_url, data=data, api_key=self._api_key)

        try:
            assert any(resp[i].status_code == 429 for i in range(len(resp)))
        except AssertionError:
            self.fail('Looks like no 429 error code. Got this {}'.format(resp))
